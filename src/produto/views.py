from django.shortcuts import render
from .normalization import atualiza_ranking

# Create your views here.
def sync(request, category_id):
    atualiza_ranking(category_id)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria, Produto, Area
from .serializers import (
    CategoriaSerializer,
    ProdutoSerializer,
    AreaSerializer
) 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def ranking(request, area_id):
    snippets = Categoria.objects.filter(area=area_id).all()
    serializer = CategoriaSerializer(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def detailed_ranking(request, area_id):
    area_query = Area.objects.filter(id=area_id).first()
    area_serializer = AreaSerializer(area_query, many=False)

    produto_query = area_query.produtos.order_by('pontuacao_geral_normalizada')
    produto_serializer = ProdutoSerializer(produto_query, many=True)

    categoria_query = area_query.categorias.all()
    categoria_serializer = CategoriaSerializer(categoria_query, many=True)

    data = {
        'Area': area_serializer.data,
        'Produto': produto_serializer.data,
        'Categoria': categoria_serializer.data
    }
    return Response(data)
