from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer          # add this
from .models import Book                # add this

# from django.http import HttpResponse
# from django.template import loader

# Create your views here.

class Todo_Book_View(viewsets.ModelViewSet):      # add this
  serializer_class = TodoSerializer                   # add this
  queryset = Book.objects.all()              # add this



# def index (request):
#     print("HttpRespone : " ,HttpResponse)
#     head_text = "Hello world sss"
#     template = loader.get_template('index.html')
#     context = {
#         'var1' : head_text 
#     }
#     return HttpResponse(template.render(context,request))
