from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)
from itertools import chain
from operator import attrgetter
from .models import Appointment

# Create your views here.
class AppointmentListView(LoginRequiredMixin, ListView):

    model = Appointment
    template_name = 'appointment_list.html'
    login_url = 'login'

    def get_queryset(self):
            qs1 = Appointment.objects.filter(Patient=self.request.user) #your first qs
            qs2 = Appointment.objects.filter(Doctor=self.request.user)  #your second qs
            #you can ad both
            queryset = sorted(chain(qs1,qs2),key=attrgetter('created_at'),)
            return queryset



class AppointmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Appointment
    template_name = 'appointment_detail.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return (obj.Patient == self.request.user, obj.Doctor == self.request.user) 


class AppointmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Appointment
    
    fields = ('Doctor', 'Patient', 'Fullname', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'Zipcode', 'Country', 'Appointment_date' , 'blood_group' ,
         'Weight' , 'Height' ,  'Blood_Sugar' , 'Blood_Pressure' , 'allergies' , 'already_taken_tablet' , 'foods_taken_before_consulation', 'complaints' ,  'department', 'status',)

    
    template_name = 'appointment_edit.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return (obj.Patient == self.request.user, obj.Doctor == self.request.user) 




class AppointmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('appointment_list')
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return (obj.Patient == self.request.user, obj.Doctor == self.request.user) 


class AppointmentCreateView(LoginRequiredMixin, CreateView):

    model = Appointment
    template_name = 'appointment_create.html'
    fields = ('Fullname', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'Zipcode', 'Country', 'Appointment_date' , 'blood_group' ,
         'Weight' , 'Height' ,  'Blood_Sugar' , 'Blood_Pressure' , 'allergies' , 'already_taken_tablet' , 'foods_taken_before_consulation', 'complaints' , 'department', 'status',)


    login_url = 'login'


    def form_valid(self, form): # new
        form.instance.Patient = self.request.user
        return super().form_valid(form)




