# Generated by Django 4.2.5 on 2023-09-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_cliente_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usname', models.CharField(max_length=100, verbose_name='Username')),
                ('firstName', models.CharField(max_length=100, verbose_name='Primeiro Nome')),
                ('lastName', models.CharField(max_length=100, verbose_name='Último Nome')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha')),
                ('emails', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('cpfs', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('telefones', models.CharField(max_length=11, verbose_name='Telefone')),
                ('enderecos', models.CharField(max_length=300)),
            ],
        ),
    ]