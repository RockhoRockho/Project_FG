# Generated by Django 3.2.5 on 2022-04-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pick', '0003_auto_20220411_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='reason',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='사유'),
        ),
    ]