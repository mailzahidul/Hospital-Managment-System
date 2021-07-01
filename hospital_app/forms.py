from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=(forms.EmailInput(attrs={'class':'form-control'})))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


# class AddDoctor(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control'}),
#             'email' : forms.EmailInput(attrs={'class':'form-control'}),
#             'phone' : forms.TextInput(attrs={'class':'form-control'}),
#             'gender' : forms.Select(attrs={'class':'form-control'}),
#             'alternative_phone' : forms.TextInput(attrs={'class':'form-control'}),
#             'second_chamber' : forms.TextInput(attrs={'class':'form-control'}),
#             'third_chamber' : forms.TextInput(attrs={'class':'form-control'}),
#             'present_address': forms.Textarea(attrs={'class':'form-control'}),
#             'parmanent_address' : forms.Textarea(attrs={'class':'form-control'}),
#             'designation' : forms.Select(attrs={'class':'form-control'}),
#         }

class AddandEditDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'alternative_phone' : forms.TextInput(attrs={'class':'form-control'}),
            'second_chamber' : forms.TextInput(attrs={'class':'form-control'}),
            'third_chamber' : forms.TextInput(attrs={'class':'form-control'}),
            'present_address': forms.Textarea(attrs={'class':'form-control'}),
            'parmanent_address' : forms.Textarea(attrs={'class':'form-control'}),
            'designation' : forms.Select(attrs={'class':'form-control'}),
        }

class AppintmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'patient' : forms.Select(attrs={'class':'form-control'}),
            'doctor' : forms.Select(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'time' : forms.TimeInput(attrs={'type':'time', 'class':'form-control'})
        }

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'relative_name' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
        }