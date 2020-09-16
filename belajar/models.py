from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()