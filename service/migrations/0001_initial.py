# Generated by Django 3.2.5 on 2022-04-13 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='받는이 이름')),
                ('content', models.TextField(blank=True, verbose_name='내용')),
                ('file', models.FileField(upload_to='', verbose_name='첨부파일')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('phone', models.CharField(max_length=30, verbose_name='폰번호')),
                ('email', models.CharField(max_length=30, verbose_name='이메일')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'verbose_name': '고객센터',
                'verbose_name_plural': '고객센터들',
                'db_table': 'service',
            },
        ),
    ]
