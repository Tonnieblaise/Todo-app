from django.db import models
from django.forms import CharField, DateTimeField


# Create your models here.
class Task(models.Model):
    '''Creating the task table in my database'''
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f"{self.name}"

    class Meta:
        ordering = ['-id']

