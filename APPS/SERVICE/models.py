from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=30, verbose_name='받는이 이름')
    content = models.TextField(blank=True, verbose_name='내용')
    file = models.FileField(verbose_name='첨부파일') #parameter?
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    phone = models.CharField(max_length=30, verbose_name='폰번호')
    email = models.CharField(max_length=30, verbose_name='이메일')
    member = models.ForeignKey('MEMBER.Member', on_delete=models.CASCADE)
    #관리자 테이블?
    class Meta:
        db_table = 'service' 
        verbose_name='고객센터' 
        verbose_name_plural='고객센터들' #???

    def __str__(self):
        return f'{self.pk} : {self.title}'