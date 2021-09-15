from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Author, Article
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id,'
            'username', 
            'email', 
            'is_staff',
            'is_active'
            ]
 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'photo'
            ]
 

class ArticlePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title', 
            'category',
            'slug',
            'sumary'            
            ] 

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title', 
            'author_id',
            'slug',
            'category',
            'sumary',            
            'fist_paragraph',
            'body'
            ]