import imp
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="log_out"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]
