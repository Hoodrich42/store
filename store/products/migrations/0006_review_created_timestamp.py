# Generated by Django 5.1.4 on 2025-01-05 13:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_rewiew_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
