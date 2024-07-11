from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Reaction, Category
from django.http import JsonResponse
from django.db.models import Count, Case, When, IntegerField
from forms import QuestionForm, CommentForm
from comments.models import Comment
from django.views.decorators.http import require_POST 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    """
        First get all questions with the latest (one that was added last) on top.
        Render the home template passing questions into context.
    """

    #Get query parameters for the search input, the question_id and category_id
    query = request.GET.get('q', '')
    highlighted_question_id = request.GET.get('question_id')
    category_id = request.GET.get('category_id')

    # Initialize the question form
    question_form = QuestionForm()
    

    if query:
        #if there is a search query
        #return only questions whose title and or content contains what is in the search
        question_list = Question.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('reactions', filter=Q(reactions__reaction='like'), distinct=True),
            dislike_count=Count('reactions', filter=Q(reactions__reaction='dislike'), distinct=True)
        ).order_by('-created_at')
    elif category_id:
        question_list = Question.objects.filter(
            category__id=category_id
        ).annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('reactions', filter=Q(reactions__reaction='like'), distinct=True),
            dislike_count=Count('reactions', filter=Q(reactions__reaction='dislike'), distinct=True)
        ).order_by('-created_at')

    else:
        question_list = Question.objects.all().annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('reactions', filter=Q(reactions__reaction='like'), distinct=True),
            dislike_count=Count('reactions', filter=Q(reactions__reaction='dislike'), distinct=True)
        ).order_by('-created_at')
    
    category_list = Category.objects.all()


    paginator = Paginator(question_list, 10)
    category_paginator = Paginator(category_list, 10)

    page = request.GET.get('page')
    category_page = request.GET.get('category_page')

    # Find the position of the highlighted question
    if highlighted_question_id:
        highlighted_question = get_object_or_404(Question, id=highlighted_question_id)
        position = list(question_list).index(highlighted_question) + 1  # +1 to get 1-based index
        # Calculate the page number
        page = (position - 1) // paginator.per_page + 1

    try:
        questions = paginator.page(page)    
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    try:
        categories = category_paginator.page(category_page)        
    except PageNotAnInteger:
        categories = category_paginator.page(1)
    except EmptyPage:
        categories= category_paginator.page(category_paginator.num_pages)

    return render(request, 'questions/home.html',{'questions': questions, 'form':question_form, 'categories':categories, 'query':query, 'question_id':highlighted_question_id})


    # questions = Question.objects.annotate(comment_count=Count('comments')).order_by('-created_at')
    # return render(request, 'questions/home.html',{'questions': questions, 'form':question_form})

def question_detail(request, pk):
    """
        Get the question whose primarykey is passed or return the notfound page.
        Render the question details template with the selected question in context.
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'questions/details.html', {'question':question})

def get_comments(request):
    question_id = request.GET.get('question_id')
    comments = Comment.objects.filter(question_id=question_id).order_by('created_at')
    return render(request, 'partials/comments.html', {'comments': comments, 'question_id': question_id})

@require_POST
def add_comment(request):
    question_id = request.POST.get('question_id')
    print(question_id)
    question = Question.objects.get(id=question_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.question = question
        comment.author = request.user
        comment.save()
        return render(request, 'partials/comment.html', {'comment': comment})
    return JsonResponse({'error': form.errors}, status=400)

def react_to_question(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        reaction_type = request.POST.get('reaction')
        question = get_object_or_404(Question, pk=question_id)
        user = request.user

        reaction, created =  Reaction.objects.get_or_create(
            user=user,
            question=question,
            defaults={'reaction': reaction_type}
        )

        if not created:
            reaction.reaction = reaction_type
            reaction.save()
        like_count = Reaction.objects.filter(question__id=question_id,reaction="like").count()
        dislike_count = Reaction.objects.filter(question__id=question_id,reaction="dislike").count()

        return JsonResponse({'like_count': like_count, 'dislike_count': dislike_count})
    return JsonResponse({}, status=400)


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
        return redirect('home')


@login_required
def update_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            print(form.errors)
            return JsonResponse({'success': False, 'errors': form.errors })
    print('Metho not supported')
    return JsonResponse({'success': False})

def delete_question(request, id):
    if request.method == 'DELETE':
        question = get_object_or_404(Question, id=id)
        if request.user == question.author:  # Ensure the user is the author
            question.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'You do not have permission to delete this question.'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    question = comment.question
    if request.user == comment.author or request.user == question.author:
        comment.delete()
        return redirect("/")
    else:
        return HttpResponseForbidden()

@login_required
def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    new_comment = request.POST.get("content")
    Comment.objects.filter(id=id).update(content=new_comment)
    return JsonResponse({'success': True})
   
