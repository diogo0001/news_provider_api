from .models import Author
from rest_framework import  status, permissions, generics
from .serializer import AuthorSerializer, ArticleSerializer, UserSerializer
from .models import Author, Article
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny 
from django.contrib.auth.models import User



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


def get_filtered_data(serialized_data, fields):
    output_data = [] 

    for d in serialized_data:
        data = {}
        for field in fields:
            if field in d:
                data[field] = d[field]
        output_data.append(data)
    
    return output_data


@api_view(['GET',])
def api_authors_view(request):
    try:
        authors = Author.objects.all()
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_articles_view(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article, many=True)
        fields = [
            'id',
            'author',
            'category',
            'title',             
            'sumary'
            ]
        
        output_data = get_filtered_data(serializer.data, fields)            
        return Response(output_data)


@api_view(['GET',])
def api_article_slug_detail_view(request,slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        fields = [
            'id',
            'author',
            'category',
            'title',             
            'sumary',
            'fist_paragraph'
            ]

        if request.user.is_authenticated:
            print("USER ALLOWED")
            fields.append('body')

    output_data = get_filtered_data([serializer.data], fields)            
    return Response(output_data)


