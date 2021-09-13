from django.contrib import admin
from .models import Author, Article

# admin.site.register(Author)
# admin.site.register(Article)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','image_url')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author_id')
    prepopulated_fields = {'slug':('title',)}