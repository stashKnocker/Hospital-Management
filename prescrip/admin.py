from django.contrib import admin
from .models import Prescription
# Register your models here.

# Register your models here.
class Prescription_detail_Admin(admin.ModelAdmin):
    list_display = ['date','Fullname', 'doctor', 'Gender', 'Age', 'case', 'prescription', 'prescription_pdf', ]
    model = Prescription
    last_filter = ['Fullname', 'case', 'Gender']
    search_fields = ['date','Fullname', 'doctor', 'Gender', 'Age', 'case', 'prescription', 'prescription_pdf', ]



# Register your models here.
admin.site.register(Prescription, Prescription_detail_Admin)