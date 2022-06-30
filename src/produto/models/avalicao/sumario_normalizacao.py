from django.db import models
# from ..produto import Produto
# from ..sub_categoria import Subcategoria
from .sumario import Sumario

class SumarioNormalizacao(models.Model):
    sumario = models.ForeignKey(
        Sumario,
        on_delete=models.SET_NULL,
        related_name='sumario',
        null=True,
        blank=True
    )

    porcentagem = models.IntegerField()

    def __str__(self):
        nome_produto = self.sumario.produto.titulo
        nome_sub_categoria = self.sumario.subcategoria.titulo
        return f'{self.porcentagem} {nome_produto} - {nome_sub_categoria}'