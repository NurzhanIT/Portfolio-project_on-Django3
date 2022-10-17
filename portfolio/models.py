from distutils.command.upload import upload
from pydoc import describe
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='portfolio/imgs/')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title