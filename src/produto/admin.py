# from django.contrib import admin
from src.django_stisla import admin as stisla

from .models import (
    Categoria,
    Produto,
    Subcategoria,
    Topico,
    Nota
)
import nested_admin

class TopicoInline(nested_admin.NestedStackedInline):
    extra = 0
    model = Topico

class SubcategoriaInline(nested_admin.NestedStackedInline):
    extra = 0
    model = Subcategoria
    inlines = [
        TopicoInline
    ]

# @admin.register(Categoria)
# @stisla.register(Categoria)
class CategoriaAdmin(nested_admin.NestedModelAdmin):
    search_fields = ['nome']

    inlines = [
        SubcategoriaInline
    ]

# stisla.site.register(Categoria)
stisla.site.register(Categoria, CategoriaAdmin)
# admin.site.register(Categoria, CategoriaAdmin)

