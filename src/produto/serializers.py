from rest_framework import serializers
from .models import Area, Categoria, Topico, Nota, Produto, Sumario

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
        'id',
        'nome',
        'soma_notas_maxima_categorias',
        'media_maxima_sumarios',
        'pontuacao_geral_maxima_sumarios'
        ]

class SumarioSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    categoria_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Sumario
        fields = [
            'id',
            'categoria',
            'categoria_id',
            'somatorio',
            'sumario',
            'sumario_normalizacao'
        ]

class ProdutoSerializer(serializers.ModelSerializer):
    sumarios = SumarioSerializer(many=True)

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'soma_todas_notas_calculadas',
            'media_sumarios',
            'pontuacao_geral_sumario',
            'media_normalizada',
            'pontuacao_geral_normalizada',
            'sumarios'
        ]

class NotasSerializer(serializers.ModelSerializer):
    produto_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    produto = serializers.StringRelatedField()

    class Meta:
        model = Nota
        fields = ['id', 'nota', 'nota_calculada', 'produto_id', 'produto']

class TopicosSerializer(serializers.ModelSerializer):
    notas = NotasSerializer(many=True)

    class Meta:
        model = Topico
        fields = ['id', 'nome', 'peso', 'nota_maxima', 'notas']


class CategoriaSerializer(serializers.ModelSerializer):
    
    topicos = TopicosSerializer(many=True)

    class Meta:
         model = Categoria
         fields = ['id', 'nome', 'soma_notas_maxima_topicos', 'max_sumario', 'topicos']