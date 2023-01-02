from django.shortcuts import render
from django.views.generic import TemplateView

class about (TemplateView):
    template_name = 'about_us.html'


