from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# ✅ Landing page
def landing_page(request):
    return render(request, 'users/landing.html')

# ✅ Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('contacts:list_contacts')  # Redirect to contact list
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return render(request, 'users/login.html')

# ✅ Register view with form and auto-login
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)  # Auto login after registration
        return redirect('contacts:list_contacts')  # Redirect to contact list
    return render(request, 'users/register.html', {'form': form})

# ✅ Home view (optional if you want a home screen)
@login_required
def home(request):
    return render(request, 'users/home.html')

# ✅ Logout view
def logout_view(request):
    logout(request)
    return redirect('users:landing')
