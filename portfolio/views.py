from django.views.generic import DetailView, TemplateView

from portfolio.models import Profile


class PortfolioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(id=1)

        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return context
