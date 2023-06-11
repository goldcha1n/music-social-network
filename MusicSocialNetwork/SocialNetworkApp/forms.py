from django import forms

from .models import Post, MusicPost

class AddPostForm(forms.ModelForm):
    post_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo_post = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Post
        fields = ('post_text', 'photo_post')


class AddMusicForm(forms.ModelForm):
    post_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    audio_post = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = MusicPost
        fields = ('post_text', 'audio_post')