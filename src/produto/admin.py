from django.contrib import admin
from src.django_stisla.admin import site
from .models import Topico

site.register(Topico)
