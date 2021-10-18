#SpeedApp\views.py


from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView
from . import forms
from . import models
# from django.shortcuts import get_object_or_404
# from django.urls import reverse_lazy
# from django.http import request

# Create your views here.
class DetectPageView(CreateView):
    form_class = forms.SpeedModelForm
    template_name = 'SpeedApp/detect.html'
    model = models.SpeedModel

class SpeedDetailView(DetailView):
    model = models.SpeedModel
    context_object_name = 'detail'
    template_name = 'SpeedApp/detail.html'