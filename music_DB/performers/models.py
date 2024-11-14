from django.db import models

# Create your models here.

class Performer(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    formation_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.genre}, {self.origin}'