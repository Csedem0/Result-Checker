from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import ParentLoginForm

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=ParentLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('results/', views.view_results, name='view_results'),
]
