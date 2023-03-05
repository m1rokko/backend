from django.contrib import admin
from .models import TodoList,Todo

admin.site.register(Todo)
admin.site.register(TodoList)
