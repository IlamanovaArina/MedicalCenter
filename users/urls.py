from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .apps import UsersConfig
from .views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
