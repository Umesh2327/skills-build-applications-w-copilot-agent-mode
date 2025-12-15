from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, LeaderboardEntry
from datetime import date

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='teamuser', password='testpass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', password='testpass')
        team = Team.objects.create(name='Activity Team')
        activity = Activity.objects.create(user=user, team=team, type='run', duration=30, date=date.today())
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.user, user)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create_user(username='leaderuser', password='testpass')
        team = Team.objects.create(name='Leaderboard Team')
        entry = LeaderboardEntry.objects.create(user=user, team=team, score=100, rank=1)
        self.assertEqual(entry.score, 100)
        self.assertEqual(entry.rank, 1)
