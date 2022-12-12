# Generated by Django 4.1.3 on 2022-12-11 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_alter_persona_email_alter_persona_rol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre')),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.estadonoticia', verbose_name='Categoría'),
        ),
    ]