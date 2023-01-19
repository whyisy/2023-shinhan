from django.db import models
from member.models import Member   #이렇게 하고 ForeignKey(member...) 바로 하면, memeber의 model.py에서도 product의 model.py를 참조하면 순환참조가 발생한다. 그래서 앱이름.모델이름 과 같은 방식 차용.

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name = "상품명")
    price = models.IntegerField(verbose_name="가격")
    product_type = models.CharField(max_length=8, verbose_name="상품유형",
        choices=(
            ('단품','단품'),
            ('세트','세트'),
        )
    )
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product'
        verbose_name='상품'
        verbose_name_plural = '상품'


    # 댓글 모델 만들기
    # 댓글에는 사용자 외래키, 상품 외래키, 댓글 내용, tstamp
    # 관리자 페이지에 등록해서
    # 관리자 페이지 통해서 댓글 3개 작성

class Comment(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name="사용자")    #앱이름.모델이름 = member.Member
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="제품")
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글'

