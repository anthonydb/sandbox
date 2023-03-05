"""anthonydb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from dotenv import load_dotenv
from django.contrib import admin
from django.urls import path, include

from .sitemap import *
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

load_dotenv()  # loads the configs from .env

# admin.autodiscover()

urlpatterns = [
    path(str(os.getenv('ADMIN_PATH')), admin.site.urls),
    path('words/', include('quotes.urls')),
    path('data-miscellany/', include('data_miscellany.urls')),
    path('sotu/', include('sotu.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt', content_type="text/plain"),
    ),
    path('', include('core.urls')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
