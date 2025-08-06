# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ User authentication and landing/home views
    path('', include('users.urls')),       # Handles: landing, login, register, logout, home

    # ✅ Contacts app (add/edit/delete/view contacts)
    path('contacts/', include('contacts.urls')),
]

