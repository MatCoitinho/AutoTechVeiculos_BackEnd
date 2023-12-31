# Generated by Django 4.2.6 on 2023-10-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculos', '0016_rename_veiculo_veiculo_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='servico',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='preco',
            field=models.IntegerField(default=0, verbose_name='Preco Do Veiculo'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='servico',
            field=models.BooleanField(default=False, verbose_name='Serviço'),
        ),
    ]
