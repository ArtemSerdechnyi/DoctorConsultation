from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
