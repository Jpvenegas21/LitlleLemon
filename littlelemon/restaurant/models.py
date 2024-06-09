from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_guest = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    booking_date = models.DateTimeField()
class Menu(models.Model):
    tittle = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()