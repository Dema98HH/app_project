from statistics import mode
from django.db import models

# Create your models here.

class Stundent(models.Model):
    name = models.CharField(max_length=140)
    course = models.CharField(max_length=140)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']

