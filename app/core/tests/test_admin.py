"""
Test for admin 
"""

from django.test  import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTestts(TestCase):
    def set_up(self):
        """ Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='sneha.saurav20@outlook.com',
            password = 'Test@123'
        )

        self.client.force_login(self.admin_user)
        self.user =get_user_model().objects.create_user(
            email='sneha.saurav20@outlook.com',
            password ='Test@123',
            name='Sneha Saurav'
        )


    def test_user_list(self):
        """ List the user """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)


