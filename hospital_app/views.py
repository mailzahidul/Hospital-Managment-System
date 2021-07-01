from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserLoginForm, AddandEditDoctorForm, AppintmentForm, AddPatientForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import *
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        print(request.user)
    return render(request, 'home.html')


class Registration(View):
    def get(self, request):
        forms = RegistrationForm()
        context = {
        'forms':forms
        }
        return render(request, 'core/registration.html', context)

    def post(self, request):
        if request.method == 'POST':
            forms = RegistrationForm(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Registration Success")
                return redirect('ragistratin')
            else:
                messages.error(request, "Validation Errors")
        context = {
            'forms':forms
        }
        return render(request, 'core/registration.html', context)


def userlogin(request):
    forms = UserLoginForm()
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Success")
                return redirect('home')
            else:
                messages.error(request, "Invalid Username or Password")
    context={
        'forms':forms
    }
    return render(request, 'core/login.html', context)


def userlogout(request):
    logout(request)
    return redirect('home')
    

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def doctor_list(request):
    doctors = Doctor.objects.order_by('id')[:5]
    context={
        'doctors':doctors
    }
    return render(request, 'doctor/doctor_list.html', context)


def add_appointment(request):
    forms = AppintmentForm()
    if request.method == 'POST':
        forms = AppintmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {
        'forms':forms
    }
    return render(request, 'appointment.html', context)

def appointment_list(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment': appointment
    }
    return render(request, 'appointment_list.html', context)


def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctor_list')


def edit_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    forms = AddandEditDoctorForm(instance=doctor)
    if request.method == 'POST':
        forms = AddandEditDoctorForm(request.POST, instance=doctor)
        forms.save()
        return redirect('doctor_list')
    context = {
        'forms':forms
    }
    return render(request, 'doctor/doctor_edit.html', context)

def view_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    context ={
        'doctor': doctor
    }
    return render(request, 'doctor/view_doctor.html', context)


def add_doctor(request):
    forms = AddandEditDoctorForm()
    if request.method == 'POST':
        forms = AddandEditDoctorForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('doctor_list')
    context={
        'forms':forms
    }
    return render(request, 'doctor/add_doctor.html', context)


def patient_list(request):
    patients = Patient.objects.all()
    context ={
        'patients' : patients
    }
    return render(request, 'patient/patient_list.html', context)


def add_patient(request):
    forms = AddPatientForm()
    if request.method == 'POST':
        forms = AddPatientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('patient_list')
    context = {
        'forms':forms
    }
    return render(request, 'patient/add_patient.html', context)