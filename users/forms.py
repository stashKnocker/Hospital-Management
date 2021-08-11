from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

USER_CHOICES = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient')
]

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES, required=True, widget=forms.RadioSelect)
    class Meta:
        fields = ("first_name", "last_name", 'username', 'email', 'user_type',)
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES, required=True, widget=forms.RadioSelect)
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", 'username', 'email', 'user_type',)


