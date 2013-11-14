# coding=utf-8
"""Models for geoscribble."""
from django.db import models


class ScribbleType(models.Model):
    """The type of a scribble."""
    name = models.CharField(
        help_text='Enter a name for a scribble type.',
        verbose_name='Type Name',
        unique=True,
        max_length=255)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Scribble(models.Model):
    """A model for scribbles."""
    name = models.CharField(max_length=255)
    scribble_date = models.DateTimeField(
        'DateAdded',
        auto_now=True,
        auto_now_add=False)
    scribble_type = models.ForeignKey(ScribbleType)

    class Meta:
        verbose_name = 'Scribble'
        verbose_name_plural = 'Scribbles'
        ordering = ('scribble_date',)

    def __unicode__(self):
        return self.name
