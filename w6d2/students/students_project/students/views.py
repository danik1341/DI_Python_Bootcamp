from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class student_list(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class student_detail(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            student = Student.objects.get(id=pk)
            if student:
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, *args, **kwargs):
        student_update = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': f'Student id - {pk} DELETED'})