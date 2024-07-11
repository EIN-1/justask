from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('get-comments/', views.get_comments, name='get_comments'),
    path('add-comment/', views.add_comment, name='add_comment'),
    path('react-to-question/', views.react_to_question, name="react_to_question"),
    path('add-question/', views.create_question, name="add-question"),
    path('delete-comment/<int:id>/', views.delete_comment, name="delete_comment"),
    path('update-question/<int:id>/', views.update_question, name="edit_question"),
    path('update-comment/<int:id>/', views.update_comment, name="edit_comment"),
    path('delete/<int:id>/', views.delete_question, name='delete_question'),
]