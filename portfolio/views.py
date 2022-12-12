from django.views.generic import DetailView, TemplateView

from portfolio.models import Profile, ResumeItem, Summary, Education, Experience


class PortfolioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(id=1)
        resume_items = ResumeItem.objects.all()
        summary = Summary.objects.all()
        education_list = Education.objects.all()
        experience_list = Experience.objects.all()

        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['resume_items'] = resume_items
        context['summary'] = summary
        context['education_list'] = education_list
        context['experience_list'] = experience_list
        return context
