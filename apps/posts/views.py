from django.shortcuts import render, redirect
from apps.posts.models import Post, PostImage, Like
from apps.posts.forms import PostForm, PostImageForm
from apps.comments.models import Comment
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all()
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Post.objects.filter(Q(title__icontains=key) |
                                    Q(description__icontains=key))
    return render(request, 'posts/index.html', {'posts': posts})

def detail(request, id=id):
    posts = Post.objects.get(id=id)
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, post=posts)
            like.delete()
        except:
            Like.objects.create(user=request.user, post=posts)

    if 'comment' in request.POST:
            try:
                text = request.POST.get('text')
                comment_obj = Comment.objects.create(user=request.user, post=posts, text=text)
                return redirect('detail_data', posts.id)
            except:
                print("Error")
    return render(request, 'posts/detail.html', {"posts": posts})

def create(request):
    form = PostForm(request.POST or None)
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1)
    if request.method == 'POST':
        if form.is_valid():
            post = Post()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post.save()
            formset = PostImageFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()
            return redirect('index')
    formset = PostImageFormSet()
    return render(request, 'posts/create.html', locals())

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