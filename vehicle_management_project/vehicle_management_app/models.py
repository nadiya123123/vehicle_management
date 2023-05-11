from django.db import models

# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Two Wheelers', 'Two Wheelers'),
        ('Three Wheelers', 'Three Wheelers'),
        ('Four Wheelers', 'Four Wheelers'),
    )

    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.TextField()