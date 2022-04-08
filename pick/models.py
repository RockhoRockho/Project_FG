from django.db import models

class Pick(models.Model):
    reason = models.CharField(max_length=30, verbose_name='사유')
    comment = models.TextField(blank=True, verbose_name='덧글')
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pick' 
        verbose_name='찜' 
        verbose_name_plural='찜들'

    
    def __str__(self):
        return self.reason
