from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/form_task.html"
    success_url = reverse_lazy("tasks:list_task")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task Created Successfully")
        return super().form_valid(form)
    
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list_task.html"
    context_object_name = 'tasks'
    
    def get_queryset(self):       
        query_set =  Task.objects.filter(user=self.request.user)
        
        q = self.request.GET.get("q")
        status = self.request.GET.get("status")
        
        if q:
            query_set = query_set.filter(title__icontains=q)
        if status:
            query_set = query_set.filter(status=status)
        
        return query_set.order_by("-created_at")
        
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/form_task.html"
    success_url = reverse_lazy("tasks:list_task")
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:list_task")
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)