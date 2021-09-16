from django.db import models
from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Author, Article
 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'id',
            'username', 
            'email', 
            'is_staff',
            'is_active',
            'password'
            ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'photo',
            ]
            

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'category',
            'title',             
            'sumary',            
            'fist_paragraph',
            'body'
            ]


 