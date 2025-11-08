from django.contrib import admin
from .models import Author,Genres,Book,Customer

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name','bio']
admin.site.register(Author,AuthorAdmin)

class GenresAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Genres,GenresAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'author', 'price']
admin.site.register(Book,BookAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email']
admin.site.register(Customer,CustomerAdmin)
    