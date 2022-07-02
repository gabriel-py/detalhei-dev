from django.db import models

# from .produto import Produto
# from .topico import Topico


class Nota(models.Model):
    produto = models.ForeignKey(
        'Produto', on_delete=models.CASCADE, related_name='notas'
    )
    topico = models.ForeignKey(
        'Topico', on_delete=models.CASCADE, related_name='notas'
    )
    nota = models.DecimalField(
        max_digits=2, decimal_places=1, null=False, blank=False
    )
    nota_calculada = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )

    def __str__(self):
        return f'{self.produto} - {self.topico}: {self.nota_calculada}'
