from django.contrib import admin

# Register your models here.
from .models import Book # add this

class TodoAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'author', 'description','image_tag',) # add this

# Register your models here.
admin.site.register(Book, TodoAdmin) # add this
