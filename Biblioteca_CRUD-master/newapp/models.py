from django.db import models

class Member(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=30)
    published_date = models.DateField()
