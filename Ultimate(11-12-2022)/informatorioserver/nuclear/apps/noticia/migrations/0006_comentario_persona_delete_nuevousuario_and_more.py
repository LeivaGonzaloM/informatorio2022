# Generated by Django 4.1.3 on 2022-12-10 04:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0005_alter_noticia_fecha_alter_noticia_publicado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('contenido', models.CharField(max_length=50, verbose_name='Título')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35, verbose_name='Nombre de usuario')),
                ('nombreApellido', models.CharField(max_length=70, verbose_name='Nombre y Apellido')),
                ('email', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('perfilImage', models.ImageField(blank=True, default='usuarios/default.png', null=True, upload_to='usuarios/', verbose_name='Foto de perfil')),
                ('rol', models.IntegerField(verbose_name='Rol')),
            ],
        ),
        migrations.DeleteModel(
            name='nuevoUsuario',
        ),
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ('-fechaPublicacion',)},
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='publicado',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='texto',
        ),
        migrations.AddField(
            model_name='noticia',
            name='contenido',
            field=models.TextField(null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='fechaCreacion',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='fechaPublicacion',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Publicacion'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=35, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.persona', verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='noticia.noticia', verbose_name='Noticia'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.persona', verbose_name='Autor'),
        ),
    ]
