from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer
from .models import Department, Employee, Project, Task

# Create your views here.

class DepartmentAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data)
        else:
            department = Department.objects.get(id=pk)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = DepartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        department_update = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=department_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        department_delete = Department.objects.get(id=pk)
        department_delete.delete()
        return Response(f'Department - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)


class EmployeeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)
        else:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        employee_update = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        employee_delete = Employee.objects.get(id=pk)
        employee_delete.delete()
        return Response(f'Employee - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)


class ProjectAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        project_update = Project.objects.get(id=pk)
        serializer = ProjectSerializer(instance=project_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        project_delete = Project.objects.get(id=pk)
        project_delete.delete()
        return Response(f'Project - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)


class TaskAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        task_update = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        task_delete = Task.objects.get(id=pk)
        task_delete.delete()
        return Response(f'Task - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)