from django.db import models
from .nota import Nota
from ..topico import Topico

class NotaItens(models.Model):
    nota = models.ForeignKey(
        Nota,
        on_delete=models.SET_NULL,
        related_name='notas',
        null=True,
        blank=True
    )

    topico = models.ForeignKey(
        Topico,
        on_delete=models.SET_NULL,
        related_name='topico_itens',
        null=True,
        blank=True
    )
    
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # noqa E501

    class Meta:
        ordering = ('pk',)
        verbose_name = 'item'
        verbose_name_plural = 'itens'

    def __str__(self):
        return f'{self.pk}'