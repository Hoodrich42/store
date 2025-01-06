# Generated by Django 5.1.4 on 2025-01-06 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_products_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='type',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.typeofproduct'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sex',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.sex'),
        ),
    ]
