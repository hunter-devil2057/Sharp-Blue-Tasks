from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

class TweetViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass12345')
        self.tweet = Tweet.objects.create(user=self.user, text='A test tweet')

    def test_list_page_loads_and_shows_tweets(self):
        response = self.client.get(reverse('tweet_list'))
        self.assertContains(response, 'A test tweet')

    def test_create_requires_login(self):
        response = self.client.get(reverse('tweet_create'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('tweet_create')}")

    def test_authenticated_user_can_create_tweet(self):
        self.client.login(username='tester', password='pass12345')
        response = self.client.post(reverse('tweet_create'), {'text': 'Created from test'})
        self.assertRedirects(response, reverse('tweet_list'))
        self.assertTrue(Tweet.objects.filter(text='Created from test', user=self.user).exists())

    def test_login_page_links_to_registration(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, reverse('register'))
        self.assertContains(response, 'Create an account')

    def test_registration_creates_and_logs_in_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'SafePassword123!',
            'password2': 'SafePassword123!',
        })
        self.assertRedirects(response, reverse('tweet_list'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
