from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from .area import Area


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    area = models.ForeignKey(
        'Area', on_delete=models.SET_NULL, null=True, related_name='produtos'
    )
    soma_todas_notas_calculadas = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True
    )
    media_sumarios = models.IntegerField(null=True, blank=True)
    pontuacao_geral_sumario = models.IntegerField(null=True, blank=True)
    media_normalizada = models.IntegerField(null=True, blank=True)
    pontuacao_geral_normalizada = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome


# @receiver(post_save, sender=Produto)
# def update_nota_maxima(sender, instance, raw, **kwargs):
#     categoria = instance.categoria
