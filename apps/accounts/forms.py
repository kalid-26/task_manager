from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserLogin(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "kalid",
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "********",
            }
        )
    )
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic', 'first_name', 'last_name', 'username', 'email', 'password', 'password2']
        
        widgets = {
            # "profile_pic": forms.ImageField(
            #     attrs={
            #         "class": "form-control",
            #         "placeholder": "Kalid"
            #     }
            # ),
            
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Kalid"
                }
            ),
            
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mohammed"
                }
            ),
            
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mohammed"
                }
            ),
            
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mohammed"
                }
            ),
            
            "password1": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mohammed"
                }
            ),
            
            "password2": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mohammed"
                }
            ),
            
        }