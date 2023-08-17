from django.contrib import admin
from .models import Course, Teacher, SchoolFacility, Laboratory

# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(SchoolFacility)
admin.site.register(Laboratory)