from rest_framework import serializers
from requests.models import Request
from users.models import User
from library_items.models import LibraryItem


class RequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    library_item = serializers.PrimaryKeyRelatedField(queryset=LibraryItem.objects.all())

    class Meta:
        model = Request
        fields = ['id', 'user', 'library_item', 'request_date', 'status']

