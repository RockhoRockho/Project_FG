from datetime import date
from django.db import models


# 관리자 테이블?
# 테이블 이름 t_?

class Member(models.Model):
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
        return #???


class Address(models.Model):
    post_num = models.IntegerField(verbose_name='우편번호')
    address = models.CharField(max_length=70, verbose_name='주소')
    address_detail = models.CharField(max_length=100, verbose_name='상세주소')
    type = models.IntegerField(verbose_name='타입') #???
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'address' 
        verbose_name='주소' 
        verbose_name_plural='주소들'

    
    def __str__(self):
        return #???



class Seller(models.Model):
    name = models.CharField(max_length=30, verbose_name='판매자이름')

    class Meta:
        db_table = 'seller' 
        verbose_name='판매자' 
        verbose_name_plural='판매자들'

    
    def __str__(self):
        return #???




class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='이름')
    price = models.IntegerField(verbose_name='가격')
    stock = models.IntegerField(verbose_name='재고')
    category = models.CharField(max_length=30, verbose_name='카테고리')
    view_cnt = models.IntegerField(default=0, verbose_name='조회수')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    delivery = models.CharField(max_length=30, verbose_name='배송비')
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'product' 
        verbose_name='상품' 
        verbose_name_plural='상품들'

    
    def __str__(self):
        return #???



class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')
    delivery_address = models.CharField(max_length=30, verbose_name='배송지')
    receiver_name = models.CharField(max_length=30, verbose_name='수령인')
    receiver_phone = models.CharField(max_length=30, verbose_name='수령자전화번호')
    eta = models.DateField(verbose_name='수령예상일')
    number = models.IntegerField(verbose_name='주문번호')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'order' 
        verbose_name='주문' 
        verbose_name_plural='주문들'

    
    def __str__(self):
        return #???


class Order_items(models.Model):
    price = models.IntegerField(verbose_name='상품가격')
    quantity = models.IntegerField(verbose_name='수량')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'order_items' 
        verbose_name='상품별 주문' 
        verbose_name_plural='상품별 주문들'

    
    def __str__(self):
        return #???



class Review(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    rating = models.FloatField(verbose_name='평점')
    detail = models.TextField(blank=True, verbose_name='상세리뷰')
    view_cnt = models.IntegerField(default=0, verbose_name='조회수')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_items_id = models.ForeignKey(Order_items, on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'review' 
        verbose_name='리뷰' 
        verbose_name_plural='리뷰들'

    
    def __str__(self):
        return #???



class Present(models.Model):
    receiver_name = models.CharField(max_length=30, verbose_name='받는이 이름')
    receiver_phone = models.CharField(max_length=30, verbose_name='받는이 휴대폰번호')
    message = models.TextField(blank=True, verbose_name='메세지')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    

    class Meta:
        db_table = 'present' 
        verbose_name='선물' 
        verbose_name_plural='선물들'

    
    def __str__(self):
        return #???


class Service(models.Model):
    title = models.CharField(max_length=30, verbose_name='받는이 이름')
    content = models.TextField(blank=True, verbose_name='내용')
    file = models.FileField(verbose_name='첨부파일') #parameter?
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    phone = models.CharField(max_length=30, verbose_name='폰번호')
    email = models.CharField(max_length=30, verbose_name='이메일')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    #관리자 테이블?

    class Meta:
        db_table = 'service' 
        verbose_name='고객센터' 
        verbose_name_plural='고객센터들' #???

    
    def __str__(self):
        return #???



class Cart(models.Model):
    quantity = models.IntegerField(verbose_name='수량')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        db_table = 'cart' 
        verbose_name='장바구니' 
        verbose_name_plural='장바구니들'

    
    def __str__(self):
        return #???



class Product_img(models.Model):
    basic_file = models.FileField(verbose_name='원본파일') #parameter?
    add_file = models.FileField(verbose_name='변경파일') #parameter?
    thumbnail = models.FileField(verbose_name='썸네일') #parameter?
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_img' 
        verbose_name='제품사진' 
        verbose_name_plural='제품사진들'

    
    def __str__(self):
        return #???



class Pick(models.Model):
    reason = models.CharField(max_length=30, verbose_name='사유')
    comment = models.TextField(blank=True, verbose_name='덧글')
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pick' 
        verbose_name='찜' 
        verbose_name_plural='찜들'

    
    def __str__(self):
        return #???


class Recent_search(models.Model):
    search_word = models.CharField(max_length=30, unique=True, verbose_name='단어')
    search_date = models.DateTimeField(auto_now_add=True, verbose_name='일자')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        db_table = 'recent_search' 
        verbose_name='최근검색기록' 
        verbose_name_plural='최근검색기록들'

    
    def __str__(self):
        return #???