from django.db import models
from performers.models import Performer

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=255)
    performer = models.ForeignKey(Performer, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    length = models.CharField(max_length=15, null=True, blank=True)

    

    def __str__(self):
        return f'{self.title}, {self.genre}, {self.year}'