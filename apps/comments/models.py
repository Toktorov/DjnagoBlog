from django.db import models
from apps.posts.models import Post
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='reply_comment', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} -- {self.post.id}"


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes_comment')

    def __str__(self):
        return f"{self.user.username} -- {self.comment.id}"