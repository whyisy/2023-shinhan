from rest_framework import serializers
# from rest_framework.exceptions import ValidationError

from .models import Product, Comment, Like
class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.comment_set.all().count()
        # return Comment.objects.filter(product=obj).count()

    class Meta:
        model = Product
        fields = '__all__'  #여기서 ['id','name'] 하면 : id, name만 뜸

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required = False
    )
    
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {'member': { 'required' : False}}


class LikeCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required = False
    )
    
    def validate_member(self, value):   #유효성 검사
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Like
        fields = '__all__'
