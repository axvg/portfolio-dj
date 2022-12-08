
from django.urls import include, path
from .views import SignUpView

urlpatterns = [
    # path("login/", LoginView.as_view(), name="login-page"),
    path("signup/", SignUpView.as_view(), name="signup-page"),
]
