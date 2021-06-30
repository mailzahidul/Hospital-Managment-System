from django import forms
from django.contrib.auth.models import User
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

# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'password']

