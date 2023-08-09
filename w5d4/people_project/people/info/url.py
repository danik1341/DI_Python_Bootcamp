from . import views
from django.urls import path


urlpatterns = [
    path('person/', views.display_person, name='person-details'),
    path('people/', views.display_people, name='people-list'),
    path('all_people/', views.display_all_people, name='all-people-list'),
]