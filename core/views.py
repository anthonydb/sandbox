from django.views.generic import TemplateView
from django.http import HttpResponsePermanentRedirect
from datetime import date


# def page_not_found_view(request, exception):
#     return render(request, '404.html', status=404)

def redirect_view(request):
    response = HttpResponsePermanentRedirect('/')
    return response


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start_date = date(2018, 9, 11)
        today = date.today()
        days_elapsed = (today - start_date).days
        years_elapsed = round(days_elapsed / 365.25, 2)
        context['years_elapsed'] = years_elapsed
        return context


class SandboxPageView(TemplateView):
    template_name = "sandbox.html"


class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


class AwardsPageView(TemplateView):
    template_name = "awards.html"
