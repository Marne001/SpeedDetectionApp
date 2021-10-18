from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'
    
class InfoPage(TemplateView):
    """docstring for HomePage."""
    template_name = 'info.html'

class WorkPage(TemplateView):
    """docstring for HomePage."""
    template_name = 'work.html'

class ContactPage(TemplateView):
    """docstring for HomePage."""
    template_name = 'contact.html'