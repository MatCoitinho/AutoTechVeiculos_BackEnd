# Generated by Django 4.2.5 on 2023-09-13 21:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usuario_delete_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='O número de telefone deve ter 11 dígitos (apenas números).', regex='^\\d{11}$')], verbose_name='Telefone'),
        ),
    ]