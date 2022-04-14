# Generated by Django 3.2.5 on 2022-04-14 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_auto_20220414_1409'),
        ('product', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('rating', models.FloatField(verbose_name='별점')),
                ('detail', models.TextField(blank=True, verbose_name='상세리뷰')),
                ('view_cnt', models.IntegerField(default=0, verbose_name='조회수')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order_items')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '리뷰',
                'verbose_name_plural': '리뷰들',
                'db_table': 'review',
            },
        ),
    ]
