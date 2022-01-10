from django.test import TestCase
from django.contrib.auth import get_user_model


class modelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with email successful"""
        email = 'bruno.researchs@gmail.com'
        password = '1221tttt#'
        user = get_user_model().objects.create_user(
            email=email, 
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'bruno.researchs@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new Superuser"""
        user = get_user_model().objects.create_superuser(
            'bruno.researchs@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
