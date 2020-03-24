from django.urls import path, include
from . import views
app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', views.LogoutView, name='logout'),
]
