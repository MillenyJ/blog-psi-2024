from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    
    context ={
        "posts" : posts,
    }
    
    
    
    return render( request, 'index.html',context)

def postagem(request, id):
    post = Post.objects.all(Post, id=id)
    return render(request, 'postagem.html', {'post': post})   
