from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ParentRegistrationForm
from .models import Student, Result

# Registration view for parents
def register(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_results')
        else:
            messages.error(request, "Registration failed. Please check the details.")
    else:
        form = ParentRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# View to show student results after login
@login_required
def view_results(request):
    student = get_object_or_404(Student, user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, 'results.html', {'student': student, 'results': results})
