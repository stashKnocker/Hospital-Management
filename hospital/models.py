from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, date
from django.contrib.auth import get_user_model
from django.urls import reverse

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

MARITAL_STATUS = (
    ('Unmarried', 'Unmarried'),
    ('Married', 'Married'),
    ('Widow', 'Widow'),
)

B_G = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
)

# Create your models here.

class Appointment(models.Model):
    Patient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, related_name='patient'
    )
    Doctor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, related_name='doctor'
    )
    Fullname = models.CharField(max_length=255)
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    Age = models.PositiveIntegerField(null=True, blank=False)
    Date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=False, help_text='Please Enter the following in YYYY-MM-DD')
    Aadhar_number = models.CharField(max_length=12, unique=True)
    Marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS)
    Father_name = models.CharField(max_length=255, help_text='if not please enter husband or guardian name.')
    Mobile_number = models.CharField(max_length=10)
    Address_1 = models.CharField(max_length=900,)
    Address_2 = models.CharField(max_length=900, blank=True, null=True)
    City = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=8)
    Country = models.CharField(max_length=100)
    Appointment_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, help_text='Please Enter the following in YYYY-MM-DD')
    blood_group = models.CharField(max_length=50, choices=B_G)
    Weight = models.FloatField(null=True,blank=True)
    Height = models.FloatField(null=True,blank=True)
    Blood_Sugar = models.FloatField(null=True,blank=True)
    Blood_Pressure = models.FloatField(null=True,blank=True)
    allergies = models.CharField(max_length=900, null=True,blank=True)
    already_taken_tablet = models.CharField(max_length=900,)
    foods_taken_before_consulation = models.CharField(max_length=900,)
    complaints = models.TextField(default="", blank = False)
    department = models.CharField(max_length=150, null=True,blank=True)
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Patient - {} Doc- {} At {}".format(self.Patient, self.Doctor, self.created_at,)

    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])


