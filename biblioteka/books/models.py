from django.db import models

# Create your models here.

class Author(models.Model):
    imie =models.Charfield(max_lenth =200)
    nazwisko=models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForegeinKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to="books_covers/%Y/%m/%d" , blank=True, null=True)

    def __str__(self):
return f'{self.title} - {self.author}'