from django.db import models

# from .area import Area


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    area = models.ForeignKey(
        'Area', on_delete=models.CASCADE, related_name='categorias'
    )
    soma_notas_maxima_topicos = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        null=True,
        blank=True,
    )
    max_sumario = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
