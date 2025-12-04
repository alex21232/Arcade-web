from django.shortcuts import render
from django.views.generic import CreateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm

# Create your views here.
