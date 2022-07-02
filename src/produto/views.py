from django.shortcuts import render
from .normalization import atualiza_ranking

# Create your views here.
def sync(request, category_id):
    atualiza_ranking(category_id)
