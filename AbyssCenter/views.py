from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def login_success(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('authapp:login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
