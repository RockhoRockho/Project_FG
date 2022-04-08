from django.db import models
from product.models import Product

class Member(models.Model):
    member_id = models.AutoField(primary_key=True, verbose_name='회원ID')
    username = models.CharField(max_length=30, verbose_name='아이디')
    pw = models.CharField(max_length=30, verbose_name='비밀번호')
    name = models.CharField(max_length=30, verbose_name='이름')
    gender = models.CharField(max_length=2, verbose_name='성별')
    email = models.CharField(max_length=30, verbose_name='이메일')
    phoneNum = models.CharField(max_length=30, verbose_name='폰번호')
    birth = models.DateField(verbose_name='생년월일')
    

    class Meta:
        db_table = 'member' 
        verbose_name='회원' 
        verbose_name_plural='회원들'

    
    def __str__(self):
        return f'{self.pk} : {self.username}'


class Address(models.Model):
    post_num = models.IntegerField(verbose_name='우편번호')
    address = models.CharField(max_length=70, verbose_name='주소')
    address_detail = models.CharField(max_length=100, verbose_name='상세주소')
    type = models.IntegerField(verbose_name='타입') #???
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'address' 
        verbose_name='주소' 
        verbose_name_plural='주소들'

    
    def __str__(self):
        return f'{self.pk} : {self.post_num}'


class Recent_search(models.Model):
    search_word = models.CharField(max_length=30, unique=True, verbose_name='단어')
    search_date = models.DateTimeField(auto_now_add=True, verbose_name='일자')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        db_table = 'recent_search' 
        verbose_name='최근검색기록' 
        verbose_name_plural='최근검색기록들'

    
    def __str__(self):
        return self.search_word