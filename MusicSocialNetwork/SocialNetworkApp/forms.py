from django import forms

from .models import Post

class AddPostForm(forms.Form):
    post_date = forms.DateField()
    photo_post = forms.ImageField()
    published = forms.BooleanField()

    class Meta:
        model = Post
        fields = ('post_text', 'post_date', 'user', 'published', 'photo_post')