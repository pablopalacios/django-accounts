from django.test import TestCase

from .models import User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='ppalacios992@gmail.com', name='pablo')

    def test_gravatar_hash(self):
        expected = '7a406dae1a1c2c09818bdfe5c60bd4ae'
        observed = self.user.get_gravatar_hash()
        self.assertEqual(expected, observed)

    def test_gravatar_url(self):
        expected = 'http://www.gravatar.com/avatar/7a406dae1a1c2c09818bdfe5c60bd4ae?size=80&d=mm'
        observed = self.user.gravatar()
        self.assertEqual(expected, observed)
