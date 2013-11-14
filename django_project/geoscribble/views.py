# coding=utf-8
"""Our views for geoscribble."""
#from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    """A simple hello world view

    :param request: A request object.
    :type request: HttpRequest

    .. note:: Request is not used by this view.
    """
    return HttpResponse('<h1>Hello World</h1>')
