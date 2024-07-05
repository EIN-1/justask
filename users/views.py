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
    user = get_object_or_404(User.objects.annotate(
        like_count=Count('reaction', filter=Q(reaction__reaction='like')),
        dislike_count=Count('reaction', filter=Q(reaction__reaction='dislike')),
        comments_count=Count('comment')
    ), pk=pk)
    print(user)
    return render(request, 'users/profile.html', {'user':user})

