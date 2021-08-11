from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, date
from django.conf import settings
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
    ('Divorce', 'Divorce'),
)

CASTE_CHOICES = (
    ('General', 'General'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
)
COMMUNITY_CHOICES = (
    ('Hindu', 'Hindu'),
    ('Muslim', 'Muslim'),
    ('Christianity', 'Christianity'),
    ('Others', 'Others'),
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




class Pprofile(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    auto_increment_id = models.AutoField(primary_key=True)
    dp = models.ImageField(default='default.jpg', upload_to='media', )
    Fullname = models.CharField(max_length=255)
    Email_Address = models.EmailField()
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    Age = models.PositiveIntegerField(null=True, blank=False)
    Date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=False, help_text='Please Enter the following in YYYY-MM-DD')
    Aadhar_number = models.CharField(max_length=12, unique=True)
    Marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS)
    Father_name = models.CharField(max_length=255)
    Father_occupation = models.CharField(max_length=255)
    Father_number = models.CharField(max_length=10, blank=True, null=True, help_text= 'If minor, Please mention')
    Mother_name = models.CharField(max_length=255)
    Mother_occupation = models.CharField(max_length=255)
    Guardian_name = models.CharField(max_length=255, null=True, blank=True)
    Guardian_occupation = models.CharField(max_length=255, null=True, blank=True)
    Mobile_number = models.CharField(max_length=10)
    Address_1 = models.CharField(max_length=900,)
    Address_2 = models.CharField(max_length=900, blank=True, null=True)
    City = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=8)
    Annual_income = models.PositiveIntegerField(null=True, blank=False)
    Caste = models.CharField(max_length=50, choices=CASTE_CHOICES)
    Community = models.CharField(max_length=50, choices=COMMUNITY_CHOICES)
    Family_History = models.CharField(max_length=255)
    Dietary_Habits = models.CharField(max_length=255)
    Inter_Personal_relationship = models.CharField(max_length=255)
    Health_status_of_family_members = models.CharField(max_length=10, blank=True, null=True, help_text= 'If minor, Please mention')
    Housing_Condition = models.CharField(max_length=255)
    History_of_present_illness = models.CharField(max_length=900)
    History_of_past_illness = models.CharField(max_length=900)
    History_of_Allergy = models.CharField(max_length=900)
    Blood_Sugar = models.FloatField(null=True,blank=True)
    Blood_Pressure = models.FloatField(null=True,blank=True)
    Body_Temperature = models.FloatField(null=True,blank=True)
    Pulse_rate = models.FloatField(null=True,blank=True)
    Respiration_rate = models.FloatField(null=True,blank=True)
    blood_group = models.CharField(max_length=50, choices=B_G)
    Weight = models.FloatField(null=True,blank=True)
    Height = models.FloatField(null=True,blank=True)
    Case_in_detail = models.TextField(blank = False)
    Medical_Insurance = models.CharField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Owner- {} Patient - {} UUID- {}".format(self.owner, self.Fullname, self.Aadhar_number)
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})
