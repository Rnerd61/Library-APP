from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthorModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.CharField(max_length=200, null=False, blank=False, default='Uploads/Default_author.jpeg')

    def get_books(self):
        return self.book.all()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Authors'


class BookModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=200, null=False, blank=False, default='Uploads/Default_book.jpeg')

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.name

