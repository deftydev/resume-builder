# Generated by Django 2.0.7 on 2020-03-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_skill3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description1',
            field=models.TextField(max_length=30),
        ),
    ]
