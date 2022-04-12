from django.db import models



class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='주문일련번호', default=1)
    date = models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')
    delivery_address = models.CharField(max_length=30, verbose_name='배송지')
    detail_address = models.CharField(max_length=60, verbose_name='상세배송지', default='')
    select_list = models.CharField(max_length=30, verbose_name='배송시요구사항', default='')
    receiver_name = models.CharField(max_length=30, verbose_name='수령인')
    receiver_phone = models.CharField(max_length=30, verbose_name='수령자전화번호')
    eta = models.DateField(verbose_name='수령예상일')
    number = models.IntegerField(verbose_name='주문번호')
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'order' 
        verbose_name='주문' 
        verbose_name_plural='주문들'

    
    def __str__(self):
        return f'{self.pk} : {self.receiver_name}'



class Order_items(models.Model):
    price = models.IntegerField(verbose_name='상품가격')
    quantity = models.IntegerField(verbose_name='수량')
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'order_items' 
        verbose_name='상품별 주문' 
        verbose_name_plural='상품별 주문들'

    
    def __str__(self):
        return #???


class Cart(models.Model):
    quantity = models.IntegerField(verbose_name='수량', default=1)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)


    class Meta:
        db_table = 'cart' 
        verbose_name='장바구니' 
        verbose_name_plural='장바구니들'

    
    def __str__(self):
        return f'{self.pk} : {self.quantity}'

