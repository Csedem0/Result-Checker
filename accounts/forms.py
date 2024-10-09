from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ParentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    student_email = forms.EmailField(help_text="Enter your child's Student Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'student_email']

    def clean_student_email(self):
        student_email = self.cleaned_data['student_email']
        if not Student.objects.filter(email=student_email).exists():
            raise forms.ValidationError("No student found with the provided email.")
        return student_email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        student_email = self.cleaned_data['student_email']

        if commit:
            user.save()
            student = Student.objects.get(email=student_email)
            student.user = user  # Link the parent account to the student
            student.save()
        return user

class ParentLoginForm(AuthenticationForm):
    pass
