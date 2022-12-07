from django.urls import path
from .views import LoginView, SignUpView, PortfolioView, CVView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login-page"),
    path("signup/", SignUpView.as_view(), name="signup-page"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio-page"),
    path("cv/", CVView.as_view(), name="cv-page"),
]
