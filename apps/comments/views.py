from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.comments.models import Comment


def comment_index(request, id):
    post_object = Post.objects.get(id=id)
    comments = post_object.comment.all()
    return render(request, 'comments/index.html', {"comments": comments})


def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get("text")
        comment.text = text
        comment.save()
        return redirect('data')
    return render(request, 'comments/update.html')


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('data')
    return render(request, 'comments/delete.html')