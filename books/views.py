from django.shortcuts import render
from django.views.generic import ListView
from .models import Books


class HomePageView(ListView):
    model = Books
    template_name = 'home.html'