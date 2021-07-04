from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def listarPosts(request):
    posts = Post.objects.all()
    return render(request, 'listar.html', {'posts': posts})

def criarPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return redirect('/posts/')
    else:
        form = PostForm()
        return render(request, 'editar.html', {'form':form})

def editarPost(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('/posts/')
    else:
        form = PostForm(instance=post)
        return render(request, 'editar.html', {'form' : form, 'post' : post})

def deletarPost(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('/posts/')