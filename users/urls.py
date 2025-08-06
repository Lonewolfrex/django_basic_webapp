from django.urls import path
from . import views

app_name = 'users'  # ✅ Enables namespacing like {% url 'users:login' %}

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]

