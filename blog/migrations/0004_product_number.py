# Generated by Django 5.0 on 2023-12-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]