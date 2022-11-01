""" 
Django command to wait for database to be available.
"""
import time 
import os
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db."""

    def handle(self, *args, **options):
        """Entry pojt for command."""
        self.stdout.write("Waiting for database..")
        db_up = False
        while db_up is False:
            try:
                print(os.environ.get('DB_PASSWORD'))
                self.check(databases=['default'])
                
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable , waiting 1 second..")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Databas available'))
      