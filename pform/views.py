from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)

from .models import Pprofile

# Create your views here.
class ProfileListView(LoginRequiredMixin ,ListView):

    model = Pprofile
    template_name = 'profile_list.html'
    login_url = 'login'

class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin ,DetailView):

    model = Pprofile
    template_name = 'profile_detail.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView): # new
    model = Pprofile
   
    fields = ('auto_increment_id', 'dp', 'Fullname', 'Email_Address', 'Gender', 'Age', 'Date_of_birth', 'Aadhar_number',
                'Marital_status', 'Father_name', 'Father_occupation', 'Father_number', 'Mother_name', 'Mother_occupation',
                'Guardian_name', 'Guardian_occupation', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'District', 'Zipcode',
                'Annual_income', 'Caste', 'Community', 'Family_History', 'Dietary_Habits', 'Inter_Personal_relationship', 'Health_status_of_family_members',
                'Housing_Condition', 'History_of_present_illness', 'History_of_past_illness', 'History_of_Allergy', 'Blood_Sugar', 'Blood_Pressure', 'Body_Temperature',
                'Pulse_rate', 'Respiration_rate', 'blood_group', 'Weight', 'Height', 'Case_in_detail', 'Medical_Insurance')

    
    template_name = 'profile_edit.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView): # new
    model = Pprofile
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('profile_list')
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user

class ProfileCreateView(LoginRequiredMixin ,CreateView):

    model = Pprofile
    template_name = 'profile_create.html'
    login_url = 'login'
    fields = ('auto_increment_id', 'dp', 'Fullname', 'Email_Address', 'Gender', 'Age', 'Date_of_birth', 'Aadhar_number',
                'Marital_status', 'Father_name', 'Father_occupation', 'Father_number', 'Mother_name', 'Mother_occupation',
                'Guardian_name', 'Guardian_occupation', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'District', 'Zipcode',
                'Annual_income', 'Caste', 'Community', 'Family_History', 'Dietary_Habits', 'Inter_Personal_relationship', 'Health_status_of_family_members',
                'Housing_Condition', 'History_of_present_illness', 'History_of_past_illness', 'History_of_Allergy', 'Blood_Sugar', 'Blood_Pressure', 'Body_Temperature',
                'Pulse_rate', 'Respiration_rate', 'blood_group', 'Weight', 'Height', 'Case_in_detail', 'Medical_Insurance')

    def form_valid(self, form): # new
        form.instance.owner = self.request.user
        return super().form_valid(form)
    