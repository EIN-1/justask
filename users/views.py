from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Count, Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def view_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    # Count comments, likes, and dislikes
    comments_count = user.comments.count()
    likes_count = user.reactions.filter(reaction='like').count()
    dislikes_count = user.reactions.filter(reaction='dislike').count()
    # Get all comments, liked questions, and disliked questions
    comments = user.comments.all()
    liked_questions = user.reactions.filter(reaction='like').distinct()
    disliked_questions = user.reactions.filter(reaction='dislike').distinct()
    
    context = {
        'user': user,
        'comments_count': comments_count,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
        'comments': comments,
        'liked_questions': liked_questions,
        'disliked_questions': disliked_questions,
    }
    
    return render(request, 'users/profile.html', context)

