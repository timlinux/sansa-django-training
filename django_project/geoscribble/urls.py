# coding=utf-8
"""Url handlers for scribble app."""

from django.conf.urls import patterns

urlpatterns = patterns(
    'geoscribble.views',
    (r'^hello_world/', 'hello_world'),
)
