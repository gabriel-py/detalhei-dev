from django.db import models
from ..produto import Produto
from ..sub_categoria import Subcategoria

class Sumario(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_sumario',
        null=True,
        blank=True
    )
    subcategoria = models.ForeignKey(
        Subcategoria,
        on_delete=models.SET_NULL,
        related_name='sumarios',
        null=True,
        blank=True
    )

    porcentagem = models.IntegerField()


    def __str__(self):
        nome_produto = self.produto.titulo
        nome_sub_categoria = self.subcategoria.titulo
        return f'{self.porcentagem} {nome_produto} - {nome_sub_categoria}'