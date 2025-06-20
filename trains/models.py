from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Train(models.Model):
    pnr = models.BigIntegerField(
        unique = True,
        validators = [
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999)
        ]
    )
    name = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    source = models.CharField(max_length = 50)
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default = 0)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.booked_seats > self.total_seats:
            raise ValueError("Booked seats cannot exceed total seats.")
        super().save(*args, **kwargs)