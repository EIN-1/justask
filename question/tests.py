from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Category, Reaction
from comments.models import Comment

class QuestionViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name="General")
        self.question = Question.objects.create(
            title="Sample Question",
            content="Sample content",
            author=self.user,
            category=self.category
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Question")


    def test_create_question_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add-question'), {
            'title': 'New Question',
            'content': 'Content of new question',
            'category': self.category.id
        })
        self.assertEqual(Question.objects.count(), 2)

    def test_create_question_unauthenticated(self):
        response = self.client.post(reverse('add-question'), {
            'title': 'New Question',
            'content': 'Content of new question',
            'category': self.category.id
        })
        self.assertEqual(Question.objects.count(), 1)


class CommentViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name="General")
        self.question = Question.objects.create(
            title="Sample Question",
            content="Sample content",
            author=self.user,
            category=self.category
        )
        self.comment = Comment.objects.create(
            question=self.question,
            author=self.user,
            content="Sample Comment"
        )

    def test_add_comment_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_comment'), {
            'question_id': self.question.id,
            'content': 'New Comment'
        })
        self.assertEqual(Comment.objects.count(), 2)

    def test_delete_comment_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))
        self.assertEqual(Comment.objects.count(), 0)


class ReactionViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name="General")
        self.question = Question.objects.create(
            title="Sample Question",
            content="Sample content",
            author=self.user,
            category=self.category
        )

    def test_react_to_question_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('react_to_question'), {
            'question_id': self.question.id,
            'reaction': 'like'
        })
        self.assertEqual(Reaction.objects.count(), 1)
