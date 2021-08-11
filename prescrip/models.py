from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

# Create your models here.
class Prescription(models.Model):
    doctor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='doctor_prescription')
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='patient_prescription')
    Fullname = models.CharField(max_length=255, default='')
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='')
    Age = models.PositiveIntegerField(null=True, blank=False)
    date = models.DateField(auto_now_add=True)
    case = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    prescription_pdf = models.FileField(upload_to='media' ,null=True)
    
    def __str__(self):
        return "Presciption Doc-{} Patient-{}".format(self.doctor, self.patient)

    def get_absolute_url(self):
        return reverse('prescription_detail', args=[str(self.id)])