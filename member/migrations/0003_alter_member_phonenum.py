# Generated by Django 3.2.5 on 2022-04-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_recent_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phoneNum',
            field=models.IntegerField(verbose_name='폰번호'),
        ),
    ]
