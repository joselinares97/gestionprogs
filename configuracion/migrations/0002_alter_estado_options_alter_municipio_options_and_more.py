# Generated by Django 5.0.6 on 2024-06-25 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tcontribuyente',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tdocumento',
            options={'managed': False},
        ),
    ]
