# Generated by Django 5.0 on 2023-12-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='grade',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
