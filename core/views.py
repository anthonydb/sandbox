from django.views.generic import TemplateView
from django.http import HttpResponsePermanentRedirect


# def page_not_found_view(request, exception):
#     return render(request, '404.html', status=404)

def redirect_view(request):
    response = HttpResponsePermanentRedirect('/')
    return response


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class SandboxPageView(TemplateView):
    template_name = "sandbox.html"


class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


class AwardsPageView(TemplateView):
    template_name = "awards.html"
