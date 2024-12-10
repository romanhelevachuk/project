from django.urls import path
from .views import AuthorListCreateView

urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='author-list-create'),
]
