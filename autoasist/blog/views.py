from django.shortcuts import render
from .models import Novinky
from django.views import generic

class PostList(generic.ListView):
        queryset =Novinky.objects.filter(status=0).order_by('-date')

        template_name = 'home.html'



