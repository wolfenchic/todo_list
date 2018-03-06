from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TodoItem

def get_todo_items(request):
   
    items = TodoItem.objects.all()
    return render(request, "todo/todo_items.html", {"items": items})

# Create your views here.
