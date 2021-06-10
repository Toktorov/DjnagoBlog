from django.urls import path
from apps.posts.views import index, create, detail

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail<int:id>/', detail, name='detail'),
]