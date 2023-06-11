from django import forms

from .models import Post

class AddPostForm(forms.ModelForm):
    post_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo_post = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Post
        fields = ('post_text', 'photo_post')