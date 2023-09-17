# Generated by Django 4.2.4 on 2023-09-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculos', '0004_veiculo_dono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='ultimaRevisao',
        ),
        migrations.AlterField(
            model_name='modelo',
            name='tipoCombustivel',
            field=models.CharField(choices=[('Gasol', 'Gasolina'), ('alco', 'Alcool'), ('Flex', 'Flex')], default='Undefined', max_length=20, verbose_name='Tipo Combustível'),
        ),
    ]