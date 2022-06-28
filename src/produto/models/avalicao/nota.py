from django.db import models
from ..produto import Produto

class Nota(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_itens',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        return f'{self.titulo}'