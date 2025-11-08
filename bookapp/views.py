
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from.serializers import AuthorSerializer,GenreSerializer,BookSerializer,CustomerSerializer
from.models import Author,Genres,Book,Customer
from rest_framework.decorators import action
from rest_framework import status

# Create your views here

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

 
class GenreViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        customer = self.get_object()
        book_ids = request.data.get('book_ids', [])

        if not book_ids:
            return Response(
                {'detail': 'Please provide book_ids.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        added_books = []

        for book_id in book_ids:
            book = Book.objects.filter(pk=book_id).first()
            if book and not customer.purchased_books.filter(pk=book.pk).exists():
                customer.purchased_books.add(book)
                added_books.append(book.title)

        if not added_books:
            return Response(
                {'detail': 'No new books added. Maybe already purchased or invalid IDs.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'detail': f'Successfully purchased {len(added_books)} book(s): {added_books}'},
            status=status.HTTP_200_OK
        )
