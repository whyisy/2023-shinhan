from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    # on_delete=models.SET_NULL   :원래 사용자가 지워지면, product 비워줘
    # on_delete=models.SET_DEFAULT   :원래 사용자가 지워지면, product 얘로 넣어줘
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="회원")   #CASCADE = 사용자가 del(탈퇴)하면, 관련 자료도 같이 다 지워진다
    title = models.CharField(max_length=128, verbose_name='상품명')
    content = models.TextField(verbose_name='상품내용')
    price = models.IntegerField(verbose_name='가격')
    location = models.CharField(max_length=256, verbose_name='위치')

    # 중간에 추가했기 때문에 makemigrations, migrate 실행
    image = models.FileField(null=True, blank=True, verbose_name='이미지')   #null:null이 가능한지 아닌지 blank: 빈칸이 가능한지 아닌지

    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'