from django.test import TestCase
from django.contrib.auth.models import User


class BaseTestCase(TestCase):

    def setUp(self):

        super(BaseTestCase, self).setUp()

        # dummy credentials for success test cases
        self.username = 'angel'
        self.email = 'angel@gmail.com'
        self.password = 'mypass'

        # creating test user
        self.user = User.objects.create_user(
                username=self.username, email=self.email,
                password=self.password)
