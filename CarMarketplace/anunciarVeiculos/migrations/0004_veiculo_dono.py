# Generated by Django 4.2.4 on 2023-09-12 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usuario_delete_cliente'),
        ('anunciarVeiculos', '0003_veiculo_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.usuario', verbose_name='Dono'),
        ),
    ]
