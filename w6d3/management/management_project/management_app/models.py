from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    projects = models.ManyToManyField("Project", related_name='employees', blank=True)
    
    def __str__(self):
        return f"Employee: {self.name}, email: {self.email}, phone number: {self.phone_number}"

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Task: {self.name} from Project - {self.project}"

