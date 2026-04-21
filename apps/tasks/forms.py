from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control"
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }
    def clean_title(self):
        title = self.cleaned_data.get("title")
        
        if not title:
            raise forms.ValidationError("Title is required")
        
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 character long")
        
        return title
    
