# coding=utf-8
"""Tests for the geoscribble application."""
from django.test import TestCase

# Create your tests here.
from models import Scribble, ScribbleType


class ScribbleTest(TestCase):
    """Unit test for the Scribble model"""
    fixtures = ['test_data.json']

    def test_creation(self):
        """Test Scribble creation"""
        count = Scribble.objects.all().count()
        scribble = Scribble()
        scribble_type = ScribbleType(name='Wonky')
        scribble_type.save()
        scribble.name = 'Test Scribble'
        scribble.scribble_type = scribble_type
        scribble.save()
        for scribble in Scribble.objects.all():
            print scribble.name
        message = 'Expected one more doodle after creation'
        assert Scribble.objects.all().count() > count, message
