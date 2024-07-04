from django.shortcuts import render, get_object_or_404, redirect
from .models import Question

# Create your views here.
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/home.html',{'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'questions/details.html', {'question':question})