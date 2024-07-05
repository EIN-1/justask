from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('get-comments/', views.get_comments, name='get_comments'),
    path('add-comment/', views.add_comment, name='add_comment')
]