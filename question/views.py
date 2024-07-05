from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.db.models import Count
from forms import QuestionForm, CommentForm
from comments.models import Comment
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    """
        First get all questions with the latest (one that was added last) on top.
        Render the home template passing questions into context.
    """
    question_form = QuestionForm()
    questions = Question.objects.annotate(comment_count=Count('comments')).order_by('-created_at')
    return render(request, 'questions/home.html',{'questions': questions, 'form':question_form})

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