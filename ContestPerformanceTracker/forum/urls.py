from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.view_post, name='post'),
    path('<slug:slug>/',views.post_detail,name='postdetail'),
  
]