# Generated by Django 4.1.3 on 2022-12-11 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0008_estadonoticia_alter_noticia_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='estado',
            new_name='estadonoticia',
        ),
    ]
