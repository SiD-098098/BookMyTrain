from django.db import models
from django.contrib.auth.models import User
from trains.models import Train


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    train = models.ForeignKey(Train, on_delete = models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_timestamp = models.DateTimeField(auto_now=True)
