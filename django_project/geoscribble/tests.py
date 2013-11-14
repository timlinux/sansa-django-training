# coding=utf-8
"""Tests for the geoscribble application."""
from django.test.client import RequestFactory
from django.test import TestCase

# Create your tests here.
from models import Scribble, ScribbleType
from views import hello_world
from django.test.client import Client


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
        self.assertNotEqual(Scribble.objects.all().count(), count)


class TestViews(TestCase):
    """Tests that scribble views work."""

    #noinspection PyPep8Naming
    def setUp(self):
        """very test needs access to the request factory.

           So we create it here"""
        self.factory = RequestFactory()

    def test_hello_world_view(self):
        """Test hello world view works."""
        request = self.factory.get('/hello_world/')  # url actually irrelevant
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
        expected_string = '<h1>Hello World</h1>'
        message = (
            'Unexpected response from helloWorld'
            ' - got %s, expected %s' %
            (response.content, expected_string))
        self.assertEqual(response.content, expected_string, message)

    def test_hello_world_url(self):
        """Test that the hello_world url works using django test web client.
        """
        client = Client()
        response = client.get('/hello_world/')
        self.assertEqual(response.status_code, 200)
        expected = '<h1>Hello World</h1>'
        message = (
            'Unexpected response from helloWorld'
            ' - got %s, expected %s' %
            (response.content, expected))
        self.assertEqual(response.content, expected, message)
