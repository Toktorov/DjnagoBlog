from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.posts.forms import PostForm
from django.forms import inlineformset_factory

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