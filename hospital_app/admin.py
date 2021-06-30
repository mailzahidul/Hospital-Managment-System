from django.contrib import admin
from .models import *

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation','email', 'phone', 'alternative_phone','photo']

admin.site.register(Doctor, DoctorAdmin)


admin.site.register(Designation)


admin.site.register(Patient)


admin.site.register(Gender)


admin.site.register(Appointment)