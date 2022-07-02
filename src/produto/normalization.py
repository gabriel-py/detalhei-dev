# from .models import Sumario, Area
from sre_constants import CATEGORY
from django.apps import apps

"""
1 - Atualizar nota_maxima em relação ao peso
2 - Somar todas as 'notas_maxima' de um topico 
3 - Atualizar notas em relação ao peso
4 - Realizar somatorio de notas de todos os topicos de uma categoria de um relacionado produto
5 - Realizar a soma de todas as notas de todos os topicos de todas categorias de um relacionado produto
6 - realizar a soma de todas as 'notas_maxima' de uma area
7 - calcular o sumario de cada categoria em relação as notas do produto
8 - obter a media dos sumarios de um produto
9 - obter a pontuação geral de um produto
10 - obter maior sumario de uma categoria
11 - obter a maior media dos sumarios
12 - obter a maior pontuação geral dos sumários
13 - obter o sumario normalizado de um produto em relacao a uma categoria
"""


def atualiza_ranking(area_id: int) -> None:
    Area = apps.get_model('produto.Area')
    area = Area.objects.filter(id=area_id).first()

    # categorias = area.categorias.all()

    # for categoria in categorias:
    #     topicos = categoria.topicos.all()
    #     categoria.soma_notas_maxima_topicos = 0

    #     for topico in topicos:
    #         topico.nota_maxima = float(topico.peso) * 10
    #         categoria.soma_notas_maxima_topicos += topico.nota_maxima

    #         topico.save()

    #         notas = topico.notas.all()

    #         for nota in notas:
    #             nota.nota_calculada = float(nota.nota) * float(topico.peso)
    #             nota.save()

    #     categoria.save()

    #     produtos = area.produtos.all()

    #     for produto in produtos:
    #         Sumario = apps.get_model('produto.Sumario')

    #         # produto.soma_todas_notas_calculadas = sum(
    #         #     [float(nota.nota_calculada) for nota in produto.notas.all()]
    #         # )

    #         sumario, created = Sumario.objects.get_or_create(
    #             produto=produto, categoria=categoria
    #         )
    #         somatorio = sum(
    #             [
    #                 float(nota.nota_calculada)
    #                 for nota in produto.notas.all()
    #                 if nota.topico.categoria.id == categoria.id
    #             ]
    #         )
    #         sumario.somatorio = somatorio

    #         sumario.sumario = round(
    #             somatorio / categoria.soma_notas_maxima_topicos * 100
    #         )
    #         sumario.save()

    #         categoria.max_sumario = max(
    #             [sumario.sumario for sumario in categoria.sumarios.all()]
    #         )
    #         categoria.save()

    #         sumarios = produto.sumarios.all()
    #         produto.media_sumarios = sum(
    #             [sumario.sumario for sumario in sumarios]
    #         ) / len(sumarios)
    #         produto.pontuacao_geral_sumario = round(
    #             somatorio / categoria.soma_notas_maxima_topicos * 100
    #         )

    #         produto.save()

    # area.soma_notas_maxima_topicos = sum(
    #     [
    #         float(categoria.soma_notas_maxima_topicos)
    #         for categoria in categorias
    #     ]
    # )

    # produtos = area.produtos.all()
    # area.media_maxima_sumarios = max(
    #     [produto.media_sumarios for produto in produtos]
    # )
    # area.pontuacao_geral_maxima_sumarios = max(
    #     [produto.pontuacao_geral_sumario for produto in produtos]
    # )
    # area.save()

    # for produto in produtos:
    #     produto.media_normalizada = round(
    #         produto.media_sumarios / area.media_maxima_sumarios * 100
    #     )
    #     produto.pontuacao_geral_normalizada = round(
    #         produto.pontuacao_geral_sumario
    #         / area.pontuacao_geral_maxima_sumarios
    #         * 100
    #     )
    #     produto.save()

    # for produto in area.produtos.all():
    #     pass

    update_topicos_and_notas(area)
    update_produto_and_area(area)


def update_topicos_and_notas(area):
    categorias = area.categorias.all()
    Topico = apps.get_model('produto.Topico')
    topicos = Topico.objects.prefetch_related('categoria').filter(
        categoria__in=categorias
    )
    sum_weight_categories = {}
    sum_scores = {}

    for topico in topicos:
        topico.nota_maxima = float(topico.peso) * 10
        Topico.objects.filter(id=topico.id).update(
            nota_maxima=topico.nota_maxima
        )

        if not sum_weight_categories.get(topico.categoria.id):
            sum_weight_categories[topico.categoria.id] = topico.nota_maxima
        else:
            sum_weight_categories[topico.categoria.id] += topico.nota_maxima

        for nota in topico.notas.all():
            nota_calculada = nota.nota * topico.peso
            Nota = apps.get_model('produto.Nota')
            Nota.objects.filter(id=nota.id).update(
                nota_calculada=nota_calculada
            )

            if not sum_scores.get(nota.produto.id):
                sum_scores[nota.produto.id] = nota_calculada
            else:
                sum_scores[nota.produto.id] += nota_calculada


    Categoria = apps.get_model('produto.Categoria')

    for categoria_id, somatorio in sum_weight_categories.items():
        Categoria.objects.filter(id=categoria_id).update(
            soma_notas_maxima_topicos=somatorio
        )

    Produto = apps.get_model('produto.Produto')
    for produto_id, somatorio in sum_scores.items():
        Produto.objects.filter(id=produto_id).update(
            soma_todas_notas_calculadas=somatorio
        )
    
    Area = apps.get_model('produto.Area')
    soma_notas_maxima_categorias = sum([weight for weight in sum_weight_categories.values()])
    Area.objects.filter(id=area.id).update(soma_notas_maxima_categorias=soma_notas_maxima_categorias)
    
    

def update_produto_and_area(area):
    Produto = apps.get_model('produto.Produto')
    Area = apps.get_model('produto.Area')
    Categoria = apps.get_model('produto.Categoria')
    produtos = area.produtos.all()
    categorias = area.categorias.all()
    Sumario = apps.get_model('produto.Sumario')
    Nota = apps.get_model('produto.Nota')
    medias_sumarios = []
    pontuacoes_gerais_sumario = []
    for produto in produtos:
        for categoria in categorias:
            notas = Nota.objects.prefetch_related('topicos').filter(topico__in=categoria.topicos.all()).filter(produto=produto.id).values()

            notas_calculadas = sum([nota['nota_calculada'] for nota in list(notas)])
            sumario_calculado = round(notas_calculadas / categoria.soma_notas_maxima_topicos * 100)
            sumario, created = Sumario.objects.get_or_create(produto=produto, categoria=categoria)

            if not created:
                Sumario.objects.filter(produto=produto).filter(categoria=categoria).update(somatorio=notas_calculadas, sumario=sumario_calculado)
            else:
                sumario.somatorio=notas_calculadas
                sumario.sumario=sumario_calculado
                # sumario.sumario_normalizacao = sumario_normalizacao
                sumario.save()

            produto.pontuacao_geral_sumario = round(sumario.somatorio / categoria.soma_notas_maxima_topicos * 100)
            pontuacoes_gerais_sumario.append(produto.pontuacao_geral_sumario)
            Produto.objects.filter(id=produto.id).update(pontuacao_geral_sumario=produto.pontuacao_geral_sumario)

        sumarios = produto.sumarios.all()
        produto.media_sumarios = round(sum([sumario.sumario for sumario in sumarios]) / len(sumarios))
        medias_sumarios.append(produto.media_sumarios)

        Produto.objects.filter(id=produto.id).update(media_sumarios=produto.media_sumarios)
        

    area.media_maxima_sumarios = max(medias_sumarios)
    area.pontuacao_geral_maxima_sumarios = max(pontuacoes_gerais_sumario)
    Area.objects.filter(id=area.id).update(media_maxima_sumarios=area.media_maxima_sumarios, pontuacao_geral_maxima_sumarios=area.pontuacao_geral_maxima_sumarios)

    for produto in produtos:
        produto.media_normalizada = round(produto.media_sumarios / area.media_maxima_sumarios * 100)
        produto.pontuacao_geral_normalizada = round(produto.pontuacao_geral_sumario / area.pontuacao_geral_maxima_sumarios * 100)

        for categoria in categorias:
            categoria.max_sumario = max([sumario.sumario for sumario in categoria.sumarios.all()])
            Categoria.objects.filter(id=categoria.id).update(max_sumario=categoria.max_sumario)

            sumario = Sumario.objects.filter(produto=produto).filter(categoria=categoria)
            selected_sumario = sumario.first()

            sumario_normalizacao = round(selected_sumario.sumario / categoria.max_sumario * 100)

            sumario.update(sumario_normalizacao=sumario_normalizacao)

        Produto.objects.filter(id=produto.id).update(media_normalizada=produto.media_normalizada, pontuacao_geral_normalizada=produto.pontuacao_geral_normalizada)

            