# Generated by Django 4.2.5 on 2023-09-17 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_cliente_telefone'),
        ('anunciarVeiculos', '0008_veiculo_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.cliente', verbose_name='Dono'),
        ),
    ]
