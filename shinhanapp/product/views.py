from django.shortcuts import render, redirect
from .models import Product
from django.http.response import JsonResponse
# Create your views here.

# templates 폴더 만들고 index.html
# main 함수 만들어서 상품 리스트 나오게 하기
# 상품 리스트에는 한줄로 상품명, 가격, 장소 나오게 하기

def main(request):
    products = Product.objects.all().order_by('-id')
    return render(request,"product.html", { 'products': products })

def write(request):
    if not request.user.is_authenticated:
        return redirect('/member/login')
        
    if request.method == 'POST':    #주소 하나에는 method 각각 하나씩만 존재할 수 있다.
        product = Product(
            user=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            price=request.POST.get("price"),
            location=request.POST.get("location"),
            image=request.FILES.get('image'),
        )
        # print(product.id)  #에러! 이유) id는 저장될 때 할당되는건데, 아직 저장되지 않았으니 id 값 을 출력할 수 없다.
        product.save()
        return redirect('/')

    return render(request,'product_write.html')

def detail(request, pk):
    product = Product.objects.get(pk=pk)

    ret = {
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'image': '/static/bg.jpg',
        'username': product.user.username,
    }
    if product.image:
        ret['image'] = product.image.url

    return JsonResponse(ret)
