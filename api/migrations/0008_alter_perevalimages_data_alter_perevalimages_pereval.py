# Generated by Django 5.0.7 on 2024-07-24 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_perevallevels_winter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevalimages',
            name='data',
            field=models.ImageField(null=True, upload_to='pereval_images/'),
        ),
        migrations.AlterField(
            model_name='perevalimages',
            name='pereval',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.pereval'),
        ),
    ]
