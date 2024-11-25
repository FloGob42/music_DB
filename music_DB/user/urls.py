from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('auth/register/', UserRegisterView.as_view(), name='user_register')
]
