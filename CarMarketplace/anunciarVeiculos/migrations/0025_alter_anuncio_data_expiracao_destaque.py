# Generated by Django 4.2.5 on 2023-12-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculos', '0024_anuncio_data_expiracao_destaque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='data_expiracao_destaque',
            field=models.DateTimeField(null=True, verbose_name='Data de expiração do destaque'),
        ),
    ]