from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Reaction, Category
from django.http import JsonResponse
from django.db.models import Count, Case, When, IntegerField
from forms import QuestionForm, CommentForm
from comments.models import Comment
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    """
        First get all questions with the latest (one that was added last) on top.
        Render the home template passing questions into context.
    """
    question_form = QuestionForm()
    question_list = Question.objects.annotate(
        comment_count=Count('comments', distinct=True),
        like_count=Count(Case(
            When(reactions__reaction='like', then=1),
            output_field=IntegerField(),
        )),
        dislike_count=Count(
            Case(
                When(reactions__reaction='dislike', then=1),
                output_field=IntegerField(),
            )
        )
    ).order_by('-created_at')
    category_list = Category.objects.all()

    paginator = Paginator(question_list, 10)
    category_paginator = Paginator(category_list, 10)

    page = request.GET.get('page')
    category_page = request.GET.get('category_page')

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

    return render(request, 'questions/home.html',{'questions': questions, 'form':question_form, 'categories':categories})


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

        like_count = Reaction.objects.filter(question=question, reaction="like").count()
        dislike_count = Reaction.objects.filter(question=question, reaction="dislike").count()

        return JsonResponse({'likes': like_count, 'dislikes': dislike_count})

    return JsonResponse({}, status=400)
