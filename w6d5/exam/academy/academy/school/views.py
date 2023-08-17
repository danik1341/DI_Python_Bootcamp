from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import TeacherSerializer, SchoolFacilitySerializer, LaboratorySerializer

# Create your views here.

def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    data = {
        'course_name': course.course_name,
        'course_code': course.course_code,
    }
    return JsonResponse(data)

class TeacherListAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class SchoolFacilityListAPIView(APIView):
    def get(self, request):
        facilities = SchoolFacility.objects.all()
        serializer = SchoolFacilitySerializer(facilities, many=True)
        return Response(serializer.data)

class LaboratoryListAPIView(APIView):
    def get(self, request):
        laboratories = Laboratory.objects.all()
        serializer = LaboratorySerializer(laboratories, many=True)
        return Response(serializer.data)