from rest_framework import serializers
from .models import Todo_Book

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo_Book
    print("serializer :", serializers.ModelSerializer)
    fields = ('id', 'title', 'description', 'completed')