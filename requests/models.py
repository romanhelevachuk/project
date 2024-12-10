from django.db import models
from users.models import User
from library_items.models import LibraryItem

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_item = models.ForeignKey(LibraryItem, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Request by {self.user.username} for {self.library_item.book.title}"
