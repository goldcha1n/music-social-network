from django import forms
from users.models import User
from .models import Post, MusicPost, Profile

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


class AddProfileForm1(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть Імя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}))
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Виберіть зображення'}),
        required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar')


class AddProfileForm2(forms.ModelForm):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть свій телефон'}), required=False)
    bio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть свій опис'}), required=False)
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Введіть дату свого дня народження'}), required=False)

    class Meta:
        model = Profile
        fields = ('phone', 'bio', 'birthday')