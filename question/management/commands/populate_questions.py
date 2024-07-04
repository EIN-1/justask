from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from question.models import Question
from comments.models import Comment
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Popilate the database with fake questions and comments'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        fake = Faker()

        #create fake Users
        self.stdout.write('Creating users...')
        users = []
        for _ in range(20):
            user = User.objects.create_user(
                username = fake.user_name(),
                email = fake.email(),
                password = 'password'
            )
            users.append(user)

        #create fake questions
        self.stdout.write('Creating questions...')
        questions = []
        for _ in range(80):
            question = Question.objects.create(
                title=fake.sentence(),
                content=fake.paragraphs(nb=20),
                author=random.choice(users)
            )
            questions.append(question)

        #create fake comments
        self.stdout.write('Creating comments...')
        for _ in range(400):
            Comment.objects.create(
                question=random.choice(questions),
                author=random.choice(users),
                content=fake.paragraph()
            )
        self.stdout.write('Database population completed sucessfully!!!')