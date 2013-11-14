# coding=utf-8
"""Our views for geoscribble."""
from django.shortcuts import render
from django.http import HttpResponse
from models import Scribble


def hello_world(request):
    """A simple hello world view

    :param request: A request object.
    :type request: HttpRequest

    .. note:: Request is not used by this view.
    """
    return HttpResponse('<h1>Hello World</h1>')


def show_scribbles(request):
    """Shows a list of scribbles.
    :param request: A request object.
    :type request: HttpRequest

    .. note:: Request is not used by this view.
    """
    scribbles = Scribble.objects.order_by('name')
    return render(
        request,
        'scribbles.html',
        {'scribbles': scribbles})
