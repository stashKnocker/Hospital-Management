from django.contrib import admin
from .models import Appointment
# Register your models here.

class Appointment_detail_Admin(admin.ModelAdmin):

    list_display = ['Appointment_date' ,'Fullname', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'Zipcode', 'blood_group', 'Weight', 'Height', 'Blood_Sugar', 'Blood_Pressure', 'allergies', 'already_taken_tablet', 'foods_taken_before_consulation',
        'complaints', 'department', 'status', 'created_at', 'updated_at',]
    model = Appointment
    last_filter = ['Fullname', 'Aadhar_number', 'blood_group']
    search_fields = ['Appointment_date' ,'Fullname', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'Zipcode', 'blood_group', 'Weight', 'Height', 'Blood_Sugar', 'Blood_Pressure', 'allergies', 'already_taken_tablet', 'foods_taken_before_consulation',
        'complaints', 'department', 'status', 'created_at', 'updated_at',]

admin.site.register(Appointment, Appointment_detail_Admin)


