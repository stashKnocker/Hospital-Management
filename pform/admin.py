from django.contrib import admin
from .models import Pprofile
# Register your models here.
class Basic_Admin(admin.ModelAdmin):
    list_display = ['Fullname', 'Aadhar_number', 'Date_of_birth', 'Father_name', 'District',]
    model = Pprofile
    last_filter = ['Fullname', 'Aadhar_number']
    search_fields = ['Fullname', 'Aadhar_number',]



admin.site.register(Pprofile, Basic_Admin)
