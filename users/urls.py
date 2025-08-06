from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),  # ✅ This fixes the error
]
