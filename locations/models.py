from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address