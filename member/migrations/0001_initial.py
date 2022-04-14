# Generated by Django 3.2.5 on 2022-04-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False, verbose_name='회원ID')),
                ('username', models.CharField(max_length=30, verbose_name='아이디')),
                ('pw', models.CharField(max_length=30, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('gender', models.CharField(max_length=2, verbose_name='성별')),
                ('email', models.EmailField(max_length=30, verbose_name='이메일')),
                ('phoneNum', models.IntegerField(verbose_name='폰번호')),
                ('birth', models.DateField(verbose_name='생년월일')),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원들',
                'db_table': 'member',
            },
        ),
    ]
