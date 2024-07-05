from django.db import models
from django.contrib.auth.models import User
from question.models import Question

# Create your models here.
class Comment(models.Model):
    """
    Each comment must have a question, author content and when it was created
    """
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'