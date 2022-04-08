from django.db import models


class Present(models.Model):
    receiver_name = models.CharField(max_length=30, verbose_name='받는이 이름')
    receiver_phone = models.CharField(max_length=30, verbose_name='받는이 휴대폰번호')
    message = models.TextField(blank=True, verbose_name='메세지')
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'present' 
        verbose_name='선물' 
        verbose_name_plural='선물들'

    
    def __str__(self):
        return f'{self.pk} : {self.receiver_name}'









