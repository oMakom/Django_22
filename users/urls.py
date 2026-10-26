from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.utils.translation import template

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(template_name = 'users/register.html'), name="register"),
    path("login/", LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page = 'catalog:home'), name="logout"),
    path('profile/', UserUpdateView.as_view(), name='profile_edit'),
]