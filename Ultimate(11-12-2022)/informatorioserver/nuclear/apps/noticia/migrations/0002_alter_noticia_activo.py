# Generated by Django 4.1.3 on 2022-12-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
