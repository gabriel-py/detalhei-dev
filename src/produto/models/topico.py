from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from ..normalization import atualiza_ranking


class Topico(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.CASCADE, related_name='topicos'
    )
    peso = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True
    )
    nota_maxima = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True
    )

    # def save(self, *args, **kwargs):
    #     self.nota_maxima = float(self.peso) * 10

    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


# @receiver(post_save, sender=Topico)
# def update_nota_maxima(sender, instance, created, **kwargs):
#     categoria = instance.categoria

#     atualiza_ranking(categoria=categoria)
# instance.nota_maxima = float(instance.peso) * 10
# instance.save()
