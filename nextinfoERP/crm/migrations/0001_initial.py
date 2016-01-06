# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='nome')),
                ('last_name', models.CharField(max_length=15, verbose_name='sobrenome')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.Pessoa')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=11, verbose_name='RG')),
            ],
            bases=('crm.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.Pessoa')),
                ('cnpj', models.CharField(max_length=11, unique=True, verbose_name='CNPJ')),
                ('ie', models.CharField(default='isento', max_length=20, verbose_name='IE')),
            ],
            bases=('crm.pessoa',),
        ),
    ]