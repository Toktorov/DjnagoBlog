from django.shortcuts import render, redirect
from apps.posts.models import Post, PostImage
from apps.posts.forms import PostForm, PostImageForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def detail(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {'posts': posts})


def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'posts/create.html', {'form': form})

def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/update.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('index')
    return render(request, 'posts/delete.html')