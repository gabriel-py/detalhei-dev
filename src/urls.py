# from django.contrib import admin
from src.django_stisla import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
