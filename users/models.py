from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

USER_CHOICES = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=8)

    def is_doctor(self):
        if self.user_type == 'Doctor':
            return True
        else:
            return False

    def is_patient(self):
        if self.user_type == 'Patient':
            return True
        else:
            return False
