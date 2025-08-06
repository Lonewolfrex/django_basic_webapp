from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Routes for landing page, login, register, logout, home
    path('', include('users.urls')),

    # ✅ Routes for contact management
    path('contacts/', include('contacts.urls')),
]


