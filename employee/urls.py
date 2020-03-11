from django.urls import path, include
from . import views
app_name = 'employee'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),
]
