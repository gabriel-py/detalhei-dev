from django.db import models


class Area(models.Model):
    nome = models.CharField(max_length=30)
    soma_notas_maxima_categorias = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True
    )
    media_maxima_sumarios = models.IntegerField(null=True, blank=True)
    pontuacao_geral_maxima_sumarios = models.IntegerField(
        null=True, blank=True
    )

    def __str__(self):
        return self.nome
