# Generated by Django 3.2.5 on 2022-04-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='회원ID'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phoneNum',
            field=models.IntegerField(verbose_name='폰번호'),
        ),
    ]