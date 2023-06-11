from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import AddPostForm, AddMusicForm

def home(request):
    posts = Post.objects.select_related('user__profile').all()
    comment_dict = {}

    for post in posts:
        comments = Comment.objects.filter(post=post)
        comment_dict[post.id] = comments

    return render(request, 'SocialNetworkApp/home.html', {'posts': posts, 'comment_dict': comment_dict})

def profile_user(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.select_related('user__profile').filter(user=user)
    return render(request, 'SocialNetworkApp/profile_user.html', {'user': user, 'posts': posts})

@login_required
def current_user_profile(request):
    user = request.user
    posts = Post.objects.select_related('user__profile').filter(user=user)
    return render(request, 'SocialNetworkApp/profile_user.html', {'user': user, 'posts': posts})


def music(request):
    posts = Post.objects.select_related('user__profile').all()
    music_posts = MusicPost.objects.select_related('user__profile').all()
    comment_dict = {}

    for post in posts:
        comments = Comment.objects.filter(post=post)
        comment_dict[post.id] = comments

    return render(request, 'SocialNetworkApp/music.html', {'music_posts': music_posts, 'comment_dict': comment_dict})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('SocialNetworkApp:home')
        else:
            return render(request, 'SocialNetworkApp/user_login.html', {'error': 'Неверные данные для входа'})
    return render(request, 'SocialNetworkApp/user_login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('SocialNetworkApp:home')
        else:
            # Обработка ошибки неверных данных авторизации
            pass
    return render(request, 'SocialNetworkApp/login.html')

def logout_view(request):
    logout(request)
    return redirect('SocialNetworkApp:home')

@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Привязка текущего пользователя к посту
            post.save()
            return redirect('SocialNetworkApp:home')
    else:
        form = AddPostForm()
    return render(request, 'SocialNetworkApp/addPost.html', {'form': form})

@login_required
def add_music(request):
    if request.method == 'POST':
        form = AddMusicForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Привязка текущего пользователя к посту
            post.save()
            return redirect('SocialNetworkApp:home')
    else:
        form = AddMusicForm()
    return render(request, 'SocialNetworkApp/addMusic.html', {'form': form})

