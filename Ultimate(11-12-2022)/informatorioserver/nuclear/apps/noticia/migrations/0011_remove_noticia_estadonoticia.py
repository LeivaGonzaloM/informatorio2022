# Generated by Django 4.1.3 on 2022-12-11 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0010_remove_estadonoticia_nombre_estadonoticia_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='estadonoticia',
        ),
    ]
