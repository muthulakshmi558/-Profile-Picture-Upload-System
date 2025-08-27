from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # homepage
    path('new/', views.create_profile, name='create_profile'),
    path('<int:pk>/', views.profile_detail, name='profile_detail'),
]
