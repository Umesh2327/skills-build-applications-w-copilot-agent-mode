
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import models, connection

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Define models dynamically for this command
        class Team(models.Model):
            name = models.CharField(max_length=100, unique=True)
            class Meta:
                app_label = 'octofit_tracker'

        class Activity(models.Model):
            user = models.CharField(max_length=100)
            type = models.CharField(max_length=100)
            duration = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'

        class Leaderboard(models.Model):
            user = models.CharField(max_length=100)
            team = models.CharField(max_length=100)
            points = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'

        class Workout(models.Model):
            name = models.CharField(max_length=100)
            description = models.TextField()
            class Meta:
                app_label = 'octofit_tracker'

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', type='Running', duration=30)
        Activity.objects.create(user='spiderman', type='Cycling', duration=45)
        Activity.objects.create(user='batman', type='Swimming', duration=60)
        Activity.objects.create(user='superman', type='Flying', duration=120)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', points=100)
        Leaderboard.objects.create(user='spiderman', team='Marvel', points=80)
        Leaderboard.objects.create(user='batman', team='DC', points=90)
        Leaderboard.objects.create(user='superman', team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength and flexibility')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
