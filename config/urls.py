from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from apps.accounts.forms import CustomUserLogin
from apps.accounts.views import RegisterView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URL
    path(
        'login/',
        auth_views.LoginView.as_view
        (
            template_name= "registration/login.html",
            authentication_form=CustomUserLogin
        ), 
        name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
    # Tasks app URL
    path('', include("apps.tasks.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
