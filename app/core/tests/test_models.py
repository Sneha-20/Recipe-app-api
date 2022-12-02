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

    
    def test_user_email_normalize(self):
        sample_test =[
            ['test20@EXAMPLE.COM', 'test2-@example.com'],
            ['Test20@Example.com', 'Test20@example.com'],
            ['TEST2@EXAMPLE.COM', 'TEST2@example.com'],
            ['test4@example.com', 'test4@example.com']
        ]

        for email , expected in sample_test:
            user = get_user_model.objects.create_user(email, 'Test@123')
            self.assertEqual(user.email, expected)

        


