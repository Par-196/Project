# Generated by Django 5.0 on 2023-12-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_product_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]