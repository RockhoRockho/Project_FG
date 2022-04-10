# Generated by Django 3.2.5 on 2022-04-08 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_word', models.CharField(max_length=30, unique=True, verbose_name='단어')),
                ('search_date', models.DateTimeField(auto_now_add=True, verbose_name='일자')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'verbose_name': '최근검색기록',
                'verbose_name_plural': '최근검색기록들',
                'db_table': 'recent_search',
            },
        ),
    ]