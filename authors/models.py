from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, default=1)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
