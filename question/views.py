from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.db.models import Count

# Create your views here.
def home(request):
    """
        First get all questions with the latest (one that was added last) on top.
        Render the home template passing questions into context.
    """
    questions = Question.objects.annotate(comment_count=Count('comments')).order_by('-created_at')
    return render(request, 'questions/home.html',{'questions': questions})

def question_detail(request, pk):
    """
        Get the question whose primarykey is passed or return the notfound page.
        Render the question details template with the selected question in context.
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'questions/details.html', {'question':question})