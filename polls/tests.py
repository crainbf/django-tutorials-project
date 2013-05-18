"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Poll


class PollTest(TestCase):
    def test_future_test_not_shown_as_recent(self):
        """
        was_published_recently should return false for Polls that have a pub_date that is in the future
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

