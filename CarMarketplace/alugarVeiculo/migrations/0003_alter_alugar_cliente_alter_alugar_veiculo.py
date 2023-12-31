# Generated by Django 4.2.5 on 2023-10-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_delete_cadastro'),
        ('anunciarVeiculos', '0020_remove_veiculo_preco'),
        ('alugarVeiculo', '0002_remove_alugar_data_remove_alugar_horario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alugar',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cliente', to_field='cpf', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='alugar',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anunciarVeiculos.veiculo', to_field='placa', verbose_name='Veiculo'),
        ),
    ]
