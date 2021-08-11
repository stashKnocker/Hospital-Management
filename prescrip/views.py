from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
import os
import requests
from django.conf import settings
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)

from itertools import chain
from operator import attrgetter

from .models import  Prescription

# Create your views here.


class PrescriptionListView(LoginRequiredMixin, ListView):

    model = Prescription
    template_name = 'prescription_list.html'
    login_url = 'login'

    def get_queryset(self):
            qs1 = Prescription.objects.filter(patient=self.request.user) #your first qs
            qs2 = Prescription.objects.filter(doctor=self.request.user)  #your second qs
            #both
            queryset = sorted(chain(qs1,qs2),key=attrgetter('date'),)
            return queryset

class PrescriptionDetailView(LoginRequiredMixin , UserPassesTestMixin, DetailView):

    model = Prescription
    template_name = 'prescription_detail.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return (obj.patient == self.request.user, obj.doctor == self.request.user) 

class PrescriptionUpdateView(LoginRequiredMixin , UserPassesTestMixin,UpdateView):

    model = Prescription
    template_name = 'prescription_edit.html'
    login_url = 'login'
    fields = ('patient', 'case', 'prescription', 'prescription_pdf',)

    def test_func(self): # new
        obj = self.get_object()
        return (obj.patient == self.request.user, obj.doctor == self.request.user) 


class PrescriptionDeleteView(LoginRequiredMixin ,UserPassesTestMixin,DeleteView): # new
    model = Prescription
    template_name = 'prescription_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('prescription_list')

    def test_func(self): # new
        obj = self.get_object()
        return (obj.patient == self.request.user, obj.doctor == self.request.user) 

class PrescriptionCreateView(LoginRequiredMixin ,CreateView):

    model = Prescription
    template_name = 'prescription_create.html'
    login_url = 'login'
    fields = ('patient', 'case', 'prescription', 'prescription_pdf',)

    def form_valid(self, form): # new
        form.instance.doctor = self.request.user
        return super().form_valid(form)


