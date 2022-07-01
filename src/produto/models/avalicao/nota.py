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

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Nota)
def update_ranking(sender, instance, created, **Kwargs):
    category_products = instance.produto.categoria.produtos.all()
    sub_categorias = instance.produto.categoria.subcategorias.all()

    for product in category_products:
        product_item = product.produto_itens.first()
        scores = product_item.notas.all()
        
        for score in scores:
            from src.produto.models import Topico
            topico = Topico.objects.filter(id=score.topico_id).first()

            try:
                peso = float(topico.peso)
                score.valor_calculado = float(score.valor) * peso
                score.save()

                for sub_categoria in sub_categorias:
                    query_sumario = sub_categoria.sumarios.filter(produto=product.id)
                    topicos = sub_categoria.topicos.all()
                    topicos_pesos = [float(topico.peso) * 10 
                        for topico in sub_categoria.topicos.all()
                    ]

                    max_score = sum(topicos_pesos)

                    from .sumario import Sumario
                    notas_produto = [
                        float(nota.valor_calculado) 
                        for nota in product.produto_itens.first().notas.all()
                        if nota.topico.subcategoria_id == sub_categoria.id
                    ]
                    soma_notas_calculado = sum(notas_produto)
                    sumario_calculado = round(soma_notas_calculado / max_score * 100)
                    if not query_sumario.exists():
                        new_sumario = Sumario()

                        new_sumario.produto = product
                        new_sumario.subcategoria = sub_categoria
                        new_sumario.porcentagem = sumario_calculado
                        new_sumario.save()
                    else:
                        sumario = query_sumario.first()
                        sumario.porcentagem = sumario_calculado
                        sumario.save()
                    
                    sumarios = sub_categoria.sumarios.all()
                    sumarios_porcentagens = [
                        sumario.porcentagem
                        for sumario in sumarios
                    ]
                    sumario_max_porcentagem = max(sumarios_porcentagens)

                    from .sumario_normalizacao import SumarioNormalizacao
                    for sumario in sumarios:
                        query = SumarioNormalizacao.objects.filter(
                            sumario=sumario.id
                        )

                        if not query.exists():
                            sumario_normalizacao = SumarioNormalizacao()
                            sumario_normalizacao.sumario = sumario
                            sumario_normalizacao.porcentagem = round(
                                sumario.porcentagem /
                                sumario_max_porcentagem *
                                100
                            )
                            sumario_normalizacao.save()
                        else:
                            sumario_normalizacao = query.first()
                            sumario_normalizacao.porcentagem = round(
                                sumario.porcentagem /
                                sumario_max_porcentagem *
                                100
                            )
                            sumario_normalizacao.save()



            except TypeError:
                pass
    