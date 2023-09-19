# Generated by Django 4.2.5 on 2023-09-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitarAnuncio', '0004_alter_solicitacao_tipocombust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='tipocombust',
            field=models.CharField(choices=[('gasolina', 'Gasolina'), ('alcool', 'Alcool'), ('flex', 'Flex'), ('hibrido', 'Híbrido'), ('eletrico', 'Elétrico')], default='Undefined', max_length=20, verbose_name='Combustível'),
        ),
    ]