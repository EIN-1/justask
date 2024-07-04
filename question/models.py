from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    """
        A question has a title, content, an author,
        The date and time it is created and when it is updated 
        With the number of likes it has
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title