from django.db import models
from django.contrib.auth.models import User
import uuid

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=20)
    photo = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.name
 
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.CharField(max_length=50)
    sumary = models.TextField()
    fist_paragraph = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
