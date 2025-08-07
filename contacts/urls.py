from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.list_contacts, name='list'),                # <-- Use 'list' here!
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('view/<int:contact_id>/', views.contact_detail, name='detail'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),

]
