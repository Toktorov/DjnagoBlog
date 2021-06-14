from django.contrib import admin
from apps.posts.models import Post, PostImage, Like, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Like)
admin.site.register(Follow)