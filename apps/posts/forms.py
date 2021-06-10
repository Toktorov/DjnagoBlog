from django import forms
from apps.posts.models import Post, PostImage
from django.forms import ModelForm


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }