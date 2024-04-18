from django.urls import path
from .models import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', RegstrView.as_view()),
    path('update/', UpdateuserPassword.as_view()),
    path('change/', PasswordCHange.as_view())
    # path('logout/', LogOut.as_view()),
]
#