""" 
Django command to wait for database to be available.
"""
from lib2to3.pytree import Base
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db."""

    def handle(self, args, **options):
        pass