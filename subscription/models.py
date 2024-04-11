from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Subscription"