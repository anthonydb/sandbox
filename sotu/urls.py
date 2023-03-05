from django.urls import path
from sotu.forms import search_sotu
from sotu.views import SotuAboutView, SotuListView, SotuDetailView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('list/', SotuListView.as_view()),
    path('search/', search_sotu, name='search_sotu'),
    path('speech/<int:pk>/', SotuDetailView.as_view(), name='speech_detail'), 
    path('', SotuAboutView.as_view(), name='sotu_about')
]