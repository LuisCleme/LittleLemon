from django.db import models

# Create your models here.

class Booking(models.Model):
    """Model definition for Booking."""

    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        """Unicode representation of Booking."""
        pass

class MenuItem(models.Model):
    """Model definition for Menu."""

    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    
    def __str__(self):
        """Unicode representation of Menu."""
        pass
