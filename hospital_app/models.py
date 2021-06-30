from django.db import models

# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.designation

class Gender(models.Model):
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.gender


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    alternative_phone = models.CharField(max_length=15)
    second_chamber = models.CharField(max_length=100, blank=True, null=True)
    third_chamber = models.CharField(max_length=100, blank=True, null=True)
    present_address = models.TextField()
    parmanent_address = models.TextField(blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='doctor_photo/')

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    relative_name = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.patient.name

 