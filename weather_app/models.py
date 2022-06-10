from django.db import models


# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=100)
    place_key = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f"{self.place_name} ({self.place_key})"
