from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    date = models.DateField()
    text=models.CharField(max_length=10000)
    def __str__(self):
        return self.title