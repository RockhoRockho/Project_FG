# Generated by Django 3.2.5 on 2022-04-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(max_length=30, verbose_name='판매자'),
        ),
    ]