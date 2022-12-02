"""
Django test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    """Test case"""

    def test_create_user_with_email_successfully(self):
        """Test creating a user with email success"""
        email ='sneha_developer@gmail.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )


        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        

