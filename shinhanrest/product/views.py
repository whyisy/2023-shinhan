from rest_framework import generics, mixins
from .models import Product
from .serializer import ProductSerializer
from .paginations import ProductionLargePagination

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
# ListModelMixin = query set 이라는 리스트를 만듦
# GenericAPIView = queryset을 위한 기본베이스
    serializer_class = ProductSerializer
    pagination_class = ProductionLargePagination
     
    def get_queryset(self):
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
    mixins.RetrieveModelMixin,
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