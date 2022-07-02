from django.db import models

# from .categoria import Categoria
# from .produto import Produto


class Sumario(models.Model):
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.CASCADE, related_name='sumarios'
    )
    produto = models.ForeignKey(
        'Produto', on_delete=models.CASCADE, related_name='sumarios'
    )
    somatorio = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True
    )
    sumario = models.IntegerField(null=True, blank=True)
    sumario_normalizacao = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.produto} - {self.categoria} : {self.somatorio}'
