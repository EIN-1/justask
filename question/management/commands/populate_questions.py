import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from question.models import Category, Question, Reaction
from comments.models import Comment
from faker import Faker
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        """
            This is the function that is called when the populate_questions command is run
        """
        fake = Faker()

        # Create categories
        # 1. create an empty list of categories
        # 2. Inform the user that categories are being created
        # 3. Loop 5 times
        #    3.a Create a category with a random word using faker
        #    3.b Append the created category to the categories array

        categories = []
        self.stdout.write("Generating categories....")
        for _ in range(5):
            category = Category.objects.create(name=fake.word())
            categories.append(category)

        # Create users
        # 1. create an empty list of users
        # 2. Inform the user that users are being created
        # 3. Loop 10 times
        #    3.a Create a user with a random username and email using faker and a password
        #    3.b Append the created user to the user array
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
        # 1. create an empty list of questions
        # 2. Inform the user that questions are being created
        # 3. Loop 20 times
        #    3.a Create a random time (created_at) between 1 year ago and today
        #    3.b Create a question with a random title, content, author, category and the created_at time, and a rondom author
        #    3.c Add the question to the questions list
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
        # 1. Inform the admin that reactions are being created
        # 2. Loop through all questions in the questions list
        #    2.a Loop a random number of times in the question
        #       2.a.1 Try to create a random reaction either like or dislike 
        #             by a random user or skip
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
        # 1. Inform the admin that comments are being created
        # 2. Loop through all questions in the questions list
        #    2.a Loop a random number of times in the question
        #       2.a.1 Create a comment by a random user and random content
        self.stdout.write("Generating comments....")
        for question in questions:
            for _ in range(random.randint(0, 5)):
                Comment.objects.create(
                    question=question,
                    author=random.choice(users),
                    content=fake.paragraph()
                )

        # Imform admin that the database has been populated with data successfully
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))