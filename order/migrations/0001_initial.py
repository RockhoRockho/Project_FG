# Generated by Django 3.2.5 on 2022-04-14 02:36

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
            name='TempOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='주문가격')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '주문 전 상품',
                'verbose_name_plural': '주문 전 상품들',
                'db_table': 'temp_order',
            },
        ),
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '상품별 주문',
                'verbose_name_plural': '상품별 주문들',
                'db_table': 'order_items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')),
                ('delivery_address', models.CharField(max_length=30, verbose_name='배송지')),
                ('detail_address', models.CharField(default='', max_length=60, verbose_name='상세배송지')),
                ('select_list', models.CharField(default='', max_length=30, verbose_name='배송시요구사항')),
                ('receiver_name', models.CharField(max_length=30, verbose_name='수령인')),
                ('receiver_phone', models.CharField(max_length=30, verbose_name='수령자전화번호')),
                ('number', models.IntegerField(verbose_name='주문번호')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문들',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='수량')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니들',
                'db_table': 'cart',
            },
        ),
    ]
