from rest_framework import serializers

from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  #여기서 ['id','name'] 하면 : id, name만 뜸

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


