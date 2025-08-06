from django.urls import path
from . import views


app_name = 'contacts'  # Optional: useful when using {% url 'contacts:list_contacts' %} in templates

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),               # View all contacts
    path('add/', views.add_contact, name='add_contact'),               # Add a new contact
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),  # Edit contact
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),  # Delete contact
]

