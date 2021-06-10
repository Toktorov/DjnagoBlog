from django.shortcuts import render, redirect
from apps.posts.models import Post, PostImage
from apps.posts.forms import PostForm, PostImageForm
from django.forms import inlineformset_factory

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def detail(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {'posts': posts})


def create(request):
    form = PostForm(request.POST or None)
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1)
    if request.method == 'POST':
        if form.is_valid():
            post = Post()
            post.owner = request.user
            post.description = form.cleaned_data['description']
            post.save()
            return redirect('index')
    return render(request, 'posts/create.html', locals())