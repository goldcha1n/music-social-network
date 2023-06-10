from django import forms

from .models import Post

class AddPostForm(forms.Form):
    post_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    post_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    photo_post = forms.CharField(widget=forms.ImageField(attrs={'class': 'form-control-file'}))
    # photo_post = forms.ImageField()
    # published = forms.BooleanField()

    class Meta:
        model = Post
        fields = ('post_text', 'post_date', 'photo_post', 'user', 'published')