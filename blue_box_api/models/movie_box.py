from django.db import models

class MovieBox(models.Model):
    """MovieBox join model"""
    box = models.ForeignKey("Box", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
