from django.shortcuts import render

from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile_detail.html"
    context_object_name = 'user_obj'
    
    def get_object(self):
        return self.request.user