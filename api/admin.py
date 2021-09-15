from django.contrib import admin
from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','photo')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug','sumary','category','author_id')
    prepopulated_fields = {'slug':('title',)}