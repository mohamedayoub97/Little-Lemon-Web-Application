from django.db import models
from django.utils import timezone

def default_now():
      return timezone.now()

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'  # ApplePie : 13.78

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=default_now, blank=True)

    def __str__(self):
        return self.name
