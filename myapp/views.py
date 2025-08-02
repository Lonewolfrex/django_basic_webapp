from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def landing(request):
    # Public landing page
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            # Return login page with error message if authentication failed
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # GET request, just show login form
        return render(request, 'login.html')

@login_required
def home(request):
    # Home page accessible only by authenticated users
    return render(request, 'home.html')

@login_required
def logout_view(request):
    # Log the user out and redirect to landing page
    logout(request)
    return redirect('landing')
