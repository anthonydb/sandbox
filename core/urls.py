from django.urls import path
from django.http import HttpResponse
from core.views import (
    redirect_view,
    HomePageView,
    AboutPageView,
    SandboxPageView,
    PrivacyPageView,
    AwardsPageView,
)
from django.conf import settings  # remove for production
from django.conf.urls.static import static  # remove for production


def health_check(request):
    return HttpResponse(status=200)


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page_view'),
    path('about/', AboutPageView.as_view(), name='about_page_view'),
    path('sandbox/', SandboxPageView.as_view(), name='sandbox_page_view'),
    path('privacy/', PrivacyPageView.as_view(), name='privacy_page_view'),
    path('awards/', AwardsPageView.as_view(), name='awards_page_view'),
    path('_health', health_check),
    path('admin/', redirect_view),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
