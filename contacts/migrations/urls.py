from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.list_contacts, name='list'),
    path('add/', views.add_contact, name='add'),
    path('edit/<int:pk>/', views.edit_contact, name='edit'),
    path('delete/<int:pk>/', views.delete_contact, name='delete'),
]
