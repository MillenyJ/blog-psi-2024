from django.shortcuts import render
from .models import Post


def index(request):
    Posts = Post.objects.all()
    
    context ={
        "Posts" : Posts,
    }
    return render( request, 'index.html',context)
