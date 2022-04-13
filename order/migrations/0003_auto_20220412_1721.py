# Generated by Django 3.2.5 on 2022-04-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220412_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='detail_address',
            field=models.CharField(default='', max_length=60, verbose_name='상세배송지'),
        ),
        migrations.AddField(
            model_name='order',
            name='select_list',
            field=models.CharField(default='', max_length=30, verbose_name='배송시요구사항'),
        ),
    ]
