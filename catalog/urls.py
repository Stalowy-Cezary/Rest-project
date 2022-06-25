from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, GenreViewSet, index, BookListView, BookDetailView
#routing specific Views into proper url
router = routers.DefaultRouter()
router.register(r'Books', BookViewSet)
router.register(r'Authors', AuthorViewSet)
router.register(r'Genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]
