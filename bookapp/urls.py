from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, GenreViewSet, BookViewSet, CustomerViewSet

# Create a router
router = DefaultRouter()


router.register('authors', AuthorViewSet,)
router.register('genres', GenreViewSet,)
router.register('books', BookViewSet, )
router.register('customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
