from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    user = request.user
    print("Logged in user:", user)
    print("User type:", user.user_type)

    if user.is_superuser:
        return render(request, 'accounts/admin_dashboard.html', {'user': user})

    if user.user_type == 'patient':
        return render(request, 'accounts/patient_dashboard.html', {'user': user})
    elif user.user_type == 'doctor':
        return render(request, 'accounts/doctor_dashboard.html', {'user': user})

    return redirect('login')  # fallback
