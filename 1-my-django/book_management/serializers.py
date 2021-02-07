from rest_framework import serializers
from .models import Book

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    print("serializer :", serializers.ModelSerializer)
    fields = ('id', 'title', 'description', 'completed')