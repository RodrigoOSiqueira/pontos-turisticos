# Generated by Django 2.0.1 on 2018-06-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos', '0008_auto_20180611_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]