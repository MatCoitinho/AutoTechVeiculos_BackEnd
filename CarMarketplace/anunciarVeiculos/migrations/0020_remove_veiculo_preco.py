# Generated by Django 4.2.6 on 2023-10-25 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculos', '0019_alter_veiculo_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='preco',
        ),
    ]