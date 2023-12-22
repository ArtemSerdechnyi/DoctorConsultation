from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_registration')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctors/registration.html', {'form': form})
