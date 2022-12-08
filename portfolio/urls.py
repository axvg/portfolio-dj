from django.urls import path
from .views import PortfolioView, CVView

urlpatterns = [
    path("portfolio/", PortfolioView.as_view(), name="portfolio-page"),
    path("cv/", CVView.as_view(), name="cv-page"),
]
