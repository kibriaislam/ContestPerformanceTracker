
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginview, name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.logoutview, name='logout'),
  
]