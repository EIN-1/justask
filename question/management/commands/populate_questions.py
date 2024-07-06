import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from question.models import Category, Question,Reaction
from comments.models import Comment
from faker import Faker
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create categories
        categories = []
        self.stdout.write("Generating categories....")
        for _ in range(5):
            category = Category.objects.create(name=fake.word())
            categories.append(category)

        # Create users
        users = []
        self.stdout.write("Generating users....")
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Create questions
        questions = []
        self.stdout.write("Generating questions....")
        for _ in range(20):
            created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            question = Question.objects.create(
                title=fake.sentence(),
                content=fake.paragraph(),
                author=random.choice(users),
                category=random.choice(categories),
                created_at=created_at,
                updated_at=created_at
            )
            questions.append(question)

        # Create reactions
        self.stdout.write("Generating reactions....")
        for question in questions:
            for _ in range(random.randint(0, 10)):
                try:
                    Reaction.objects.create(
                        user=random.choice(users),
                        question=question,
                        reaction=random.choice(['like', 'dislike'])
                    )
                except:
                    continue

        # Create comments
        self.stdout.write("Generating comments....")
        for question in questions:
            for _ in range(random.randint(0, 5)):
                Comment.objects.create(
                    question=question,
                    author=random.choice(users),
                    content=fake.paragraph()
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))