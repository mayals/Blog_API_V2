from rest_framework import serializers
from .models import  Category,Post,UserModel,Comment
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='blog_api:category')
    class Meta:
        model = Category
        fields = ['url','id','name','posts']
      
        extra_kwargs = {
                    'url': {
                        'view_name': 'blog_api:category',
                        'lookup_field' :'pk',
                        'read_only': True
                        },
                    'id': {'read_only': True},
                    'posts':{'read_only': True},
                    }
                   
                    



class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')  # category is foreign key field
    author = serializers.SlugRelatedField(queryset=UserModel.objects.all(), slug_field='username')  # author is foreign key field
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text')
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='blog_api:post')
    class Meta:
        model = Post
        fields = ['id','title','author','category','body','created_at','updated_at','comments','url']
        extra_kwargs = {             
                        'id': {'read_only': True},
                        'author': {'read_only': True},
                        'category': {'read_only': True},
                        'comments': {'read_only': True},
                        'created_at': {'read_only': True},
                        'updated_at': {'read_only': True},
                    }



class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')  # post is foreign key field
    class Meta:
        model = Comment
        fields = ['id','post','text','comment_by','created_at','updated_at','approved_comment']
        extra_kwargs = {
                        'id': {'read_only': True},
                        'post': {'read_only': True},
                        'comment_by': {'read_only': True},
                        'created_at': {'read_only': True},
                        'updated_at': {'read_only': True},
                    }







class UserModelSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    class Meta:
        model = UserModel
        fields = ['id','username','first_name','last_name','born_date','posts']


        # username must be read only field NOT allowed to updated !
        extra_kwargs = {             
                        'id': {'read_only': True},
                        'username': {'read_only': True},  
                        'posts': {'read_only': True},
                    }



          