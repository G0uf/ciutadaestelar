# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-25 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('naus', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('comanda_id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(auto_now=True)),
                ('carrer', models.CharField(help_text='El nom del carrer on enviarem la comanda.', max_length=50, verbose_name='Carrer')),
                ('poblacio', models.CharField(help_text='La poblaci\xf3 a la qual pertany el carrer.', max_length=30, verbose_name='Poblaci\xf3')),
                ('codi_postal', models.PositiveIntegerField(help_text='El codi postal de la poblaci\xf3.', verbose_name='Codi Postal')),
                ('provincia', models.CharField(help_text='La prov\xedncia a la qual pertany la poblaci\xf3.', max_length=30, verbose_name='Prov\xedncia')),
                ('pagament', models.CharField(choices=[('CRE', 'Credits'), ('DIN', 'Diners')], default='D', max_length=3)),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Linia',
            fields=[
                ('linia_id', models.AutoField(primary_key=True, serialize=False)),
                ('preu', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantitat', models.PositiveIntegerField()),
                ('pagament', models.CharField(choices=[('CRE', 'Credits'), ('DIN', 'Diners')], default='D', max_length=3)),
                ('comanda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrets.Comanda')),
                ('producte_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naus.Nau')),
            ],
        ),
    ]
