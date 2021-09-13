from django.db import models
from django.contrib.auth.models import User
 

class Author(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(null=False,upload_to='images')

    def __str__(self):
        return self.name
 
class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    sumary = models.TextField()
    body = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
