# Generated by Django 2.0.1 on 2018-06-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('pontos', '0004_auto_20180606_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]