"""
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from djangotoolbox.fields import ListField


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()
"""


