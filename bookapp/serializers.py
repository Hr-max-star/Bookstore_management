from rest_framework import serializers
from.models import*

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
       author = AuthorSerializer(read_only=True)
       genres = GenreSerializer(many=True, read_only=True)
       class Meta:
            model=Book
            fields=['id','title','price','author','genres']

       def validate_price(self,value):
            if value <= 0 :
                 raise serializers.ValidationError("Price must be greater than 0")
            return value
                 
class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
          model=Customer
          fields=['id', 'name', 'email', 'purchased_books']

     def validate_email(self,value):
          if not value.lower().endswith('@gmail.com'):
               raise serializers.ValidationError("Email must be end with '@gmail.com'")
          return value


                 