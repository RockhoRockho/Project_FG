# Generated by Django 3.2.5 on 2022-04-08 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_name', models.CharField(max_length=30, verbose_name='받는이 이름')),
                ('receiver_phone', models.CharField(max_length=30, verbose_name='받는이 휴대폰번호')),
                ('message', models.TextField(blank=True, verbose_name='메세지')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '선물',
                'verbose_name_plural': '선물들',
                'db_table': 'present',
            },
        ),
    ]