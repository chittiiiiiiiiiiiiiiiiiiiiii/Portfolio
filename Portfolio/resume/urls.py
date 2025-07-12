from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('resume',views.resume,name='resume'),
    path('certificates',views.certificates,name='certificates'),
    path('projects',views.projects,name='projects'),
]