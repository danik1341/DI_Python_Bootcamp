from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses_taught = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class SchoolFacility(models.Model):
    facility_name = models.CharField(max_length=100)
    usage_purpose = models.TextField()

    def __str__(self):
        return self.facility_name

class Laboratory(SchoolFacility):
    equipment_list = models.TextField()

    def __str__(self):
        return f"Laboratory: {self.facility_name}"
