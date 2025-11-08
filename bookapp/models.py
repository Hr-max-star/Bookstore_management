from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Genres(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,)
    genre=models.ManyToManyField(Genres,blank=True)

    def __str__(self):
        return f"{self.title}-{self.author.name}"
    

class Customer(models.Model):   
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    purchased_books=models.ManyToManyField(Book,blank=True)

    def __str__(self):
        return f"{self.name}-{self.email}"