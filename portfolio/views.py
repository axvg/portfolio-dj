from django.views.generic import DetailView, TemplateView

from portfolio.models import Profile


class PortfolioView(TemplateView):
    template_name = "index.html"
