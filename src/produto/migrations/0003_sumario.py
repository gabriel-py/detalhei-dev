# Generated by Django 4.0.5 on 2022-06-29 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_notaitens_valor_calculado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sumario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentagem', models.IntegerField()),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto_sumario', to='produto.produto')),
                ('subcategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sumarios', to='produto.subcategoria')),
            ],
        ),
    ]
