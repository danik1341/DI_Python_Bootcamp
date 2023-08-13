from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Profile

# Create your views here.

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            profile = Profile.objects.create(name=name, email=email, is_active=True)
            return JsonResponse({'message': 'Profile created successfully!'})
        else:
            return JsonResponse({'message': 'Invalid data provided'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    

@csrf_exempt
def delete_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return JsonResponse({'message': 'Profile deleted successfully!'})