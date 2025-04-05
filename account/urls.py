from django.urls import path
from account.views import UserRegistration, UserLoginView

urlpatterns = [
    path("register/", UserRegistration.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
