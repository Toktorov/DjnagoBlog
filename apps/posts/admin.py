from django.contrib import admin
from apps.posts.models import Post, PostImage, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Like)