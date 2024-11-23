from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls')),  # Додає маршрути з додатку authors
    path('books/', include('books.urls')),
    path('library-items/', include('library_items.urls')),
    path('users/', include('users.urls')),
    path('requests/', include('requests.urls')),
]
