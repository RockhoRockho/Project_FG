# Generated by Django 3.2.5 on 2022-04-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220411_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='물품ID'),
        ),
    ]