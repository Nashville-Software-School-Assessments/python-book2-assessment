from django.db import models

class Box(models.Model):
    location = models.CharField(max_length=75)
    business_name = models.CharField(max_length=50)

    movies = models.ManyToManyField("Movie", through="MovieBox", related_name="boxes")

