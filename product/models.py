from django.db import models

class Product(models.Model):
    product = models.IntegerField(default=0, verbose_name='물품ID', null=False)
    name = models.CharField(max_length=30, verbose_name='이름')
    price = models.IntegerField(verbose_name='가격')
    category = models.CharField(max_length=30, verbose_name='카테고리')
    view_cnt = models.IntegerField(default=0, verbose_name='조회수')
    image = models.CharField(max_length=300, verbose_name='상품이미지', default=None)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    delivery = models.CharField(max_length=30, verbose_name='배송비', default='무료배송')
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    
 
    class Meta:
        db_table = 'product' 
        verbose_name='상품' 
        verbose_name_plural='상품들'

    
    def __str__(self):
        return f'{self.pk} : {self.name}'

class Seller(models.Model):
    name = models.CharField(max_length=30, verbose_name='판매자이름')

    class Meta:
        db_table = 'seller' 
        verbose_name='판매자' 
        verbose_name_plural='판매자들'

    
    def __str__(self):
        return f'{self.name}'