from django.views.generic import TemplateView, ListView, DetailView
# from django.template import RequestContext
from django.shortcuts import render
from sotu.models import Speech


class SotuAboutView(TemplateView):
    template_name = 'sotu_about.html'


class SotuListView(ListView):
    template_name = 'sotu_list.html'
    queryset = Speech.objects.order_by('-speech_date')
    context_object_name = 'speech_list'


class SotuDetailView(DetailView):
    model = Speech
    template_name = 'sotu_detail.html'

