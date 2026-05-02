from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserLogin(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "username",
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
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@gmail.com"
            }
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "******"
            }
        )
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "******"
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = ['profile_pic', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        widgets = {
            
            "profile_pic": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "first name"
                }
            ),
            
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "last name"
                }
            ),
            
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "username"
                }
            ),
            
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("this email is already registerd!")
        
        return email.lower()