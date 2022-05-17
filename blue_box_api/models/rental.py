from django.db import models
from django.contrib.auth.models import User

class Rental(models.Model):
    """Rental Model"""
    due_date = models.DateField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
