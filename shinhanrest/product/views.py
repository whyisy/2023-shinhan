from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Product, Comment, Like  #또는 from memeber.models import Comment  #from .models import comment는 안됨(자세한 설명은 노션에)
from .serializer import (
    ProductSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeCreateSerializer

)
from .paginations import ProductionLargePagination

class ProductListView(
    mixins.ListModelMixin,   #여러개 read
    mixins.CreateModelMixin,  #한개 create
    generics.GenericAPIView
):
# ListModelMixin = query set 이라는 리스트를 만듦
# GenericAPIView = queryset을 위한 기본베이스
    serializer_class = ProductSerializer
    pagination_class = ProductionLargePagination
     
    def get_queryset(self):    #queryset : 여러 모델을 가져오는 것
        
        #인자값 받아서 filter하면 되겠네!
        
        products = Product.objects.all()

        page = self.request.query_params.get('page',1)
        
        if 'name' in self.request.query_params:
            name = self.request.query_params['name']    #앞선 코드 복붙해 왔는데 request에 에러뜸 -> self.request 하기
            products = products.filter(name__contains=name)  

        # name = self.request.query_params.get('name')     #또는 이렇게
        # if name:
        #     products = products.filter(name__contains=name)
        # else:
        #   products = Product.objects.all()

        return products.order_by('id')

     
    def get(self, request, *args, **kwargs):
        #Queryset
        #Serialize
        #return Response
        print(request.user)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class ProductDetailView(
    mixins.RetrieveModelMixin,   #한 개 read
    mixins.DestroyModelMixin,    
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)




# 주석 한번 취소 하면 복붙한 값과 뭐가 다른지 나옴~~~
# class CommentListView(
#     mixins.ListModelMixin,
#     # mixins.CreateModelMixin, 
#     generics.GenericAPIView
# ):
# # ListModelMixin = query set 이라는 리스트를 만듦
# # GenericAPIView = queryset을 위한 기본베이스
#     serializer_class = CommentSerializer
#     # pagination_class = ProductionLargePagination   #이미 pagination은 settings에 디폴트값 설정되어 있음, 이건 공부차 넣은거
     
#     def get_queryset(self):    #queryset : 여러 모델을 가져오는 것
        
#     #     #인자값 받아서 filter하면 되겠네!
        
#     #     comments = Comment.objects.all()

#     #     page = self.request.query_params.get('page',1)
        
#         # if 'name' in self.request.query_params:
#         #     name = self.request.query_params['name']    #앞선 코드 복붙해 왔는데 request에 에러뜸 -> self.request 하기
#         #     comments = comments.filter(comments__contains=comments)  

#         # name = self.request.query_params.get('name')     #또는 이렇게
#         # if name:
#         #     products = products.filter(name__contains=name)
#         # else:
#         #   products = Product.objects.all()

#         product_id = self.kwargs.get('product_id')
#         if product_id:
#             return Comment.objects.filter(product_id=product_id).order_by('-id')
#         return Comment.objects.none()
#         # return Comment.objects.all().order_by('id')   #이거는 그냥 리스트로 나올 때만

#     def get(self, request, *args, **kwargs):
#         #Queryset
#         #Serialize
#         #return Response
#         # print(request.user)
#         return self.list(request, args, kwargs)


#이건 필요한 것만 모은 거
class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product_id=product_id).order_by('-id')   #product=product_id 해도 가능
        return Comment.objects.none()

    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer
 
    # def get_queryset(self):   #안써도 됨
    #     return Comment.objects.all()

    def post(self,request, *args, **kwargs):
        return self.create(request, args, kwargs)


# class LikeView(    내가 한 거... ㅋㅋㅋ..
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     generics.GenericAPIView
# ):
#     serializer_class = CommentCreateSerializer
 
#     # def get_queryset(self):   #안써도 됨
#     #     return Comment.objects.all()

#     def post(self,request, *args, **kwargs):
#         return self.create(request, args, kwargs)

class LikeCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = LikeCreateSerializer

    def get_queryset(self):
        return Like.objects.all()

    def post(self,request, *args, **kwargs):     #좋아요 한번만 기능
        product_id = request.data.get('product')

        if Like.objects.filter(member=request.user, product_id=product_id).exists():
            Like.objects.filter(member=request.user, product_id=product_id).delete()   #좋아요 취소 기능
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return self.create(request, args, kwargs)