from django.db import models

class Review(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    rating = models.FloatField(verbose_name='별점')
    detail = models.TextField(blank=True, verbose_name='상세리뷰')
    view_cnt = models.IntegerField(default=0, verbose_name='조회수')
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    order_items_id = models.ForeignKey('order.Order_items', on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'review' 
        verbose_name='리뷰' 
        verbose_name_plural='리뷰들'

    
    def __str__(self):
        return f'{self.pk} : {self.rating}'
