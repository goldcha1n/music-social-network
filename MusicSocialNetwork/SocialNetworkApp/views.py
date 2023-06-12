from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

from .models import *
from .forms import AddPostForm, AddMusicForm, AddProfileForm

def count_likes(request, post_id):
    post = Post.objects.get(id=post_id)
    like_count = Like.objects.filter(post=post).aggregate(total_likes=Count('id'))

    total_likes = like_count['total_likes']
    return total_likes

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    total_likes = count_likes(request, post_id)
    try:
        likes = Like.objects.get(user=request.user, post=post)
    except:
        likes = None
    return render(request, 'SocialNetworkApp/post.html', {'post': post, 'total_likes': total_likes, 'likes': likes})

@login_required
def delete_post(request, post_id):
    try:
        user = Post.objects.filter(id=post_id).get(user=request.user)
    except:
        user = None
    if user:
        user.delete()
        return HttpResponseRedirect(reverse('SocialNetworkApp:current_user_profile'))
    else:
        return HttpResponseRedirect(reverse('SocialNetworkApp:home'))

@login_required
def delete_music(request, music_id):
    try:
        music = MusicPost.objects.filter(id=music_id).get(user=request.user)
    except:
        music = None
    if music:
        music.delete()
    return HttpResponseRedirect(reverse('SocialNetworkApp:music'))

def home(request):
    posts = Post.objects.order_by('-post_date')

    return render(request, 'SocialNetworkApp/home.html', {'posts': posts,})

def profile_user(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.select_related('user').filter(user=user)
    return render(request, 'SocialNetworkApp/profile_user.html', {'user': user, 'posts': posts})

@login_required
def current_user_profile(request):
    user = request.user
    posts = Post.objects.select_related('user').filter(user=user)
    return render(request, 'SocialNetworkApp/profileCurrent.html', {'user': user, 'posts': posts})


def music(request):
    posts = Post.objects.select_related('user').all()
    music_posts = MusicPost.objects.select_related('user').all()
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
            return redirect('SocialNetworkApp:music')
    else:
        form = AddMusicForm()
    return render(request, 'SocialNetworkApp/addMusic.html', {'form': form})

@login_required
def add_profile(request):
    if request.method == 'POST':
        form = AddProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('SocialNetworkApp:current_user_profile'))
    else:
        form = AddProfileForm(instance=request.user)

    posts = Post.objects.select_related('user').filter(user=request.user)
    return render(request, 'SocialNetworkApp/AddProfileUser.html', {'form': form, 'posts': posts})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Проверяем, не оставлял ли пользователь уже лайк для данной записи
    if not Like.objects.filter(post=post, user=user).exists():
        like = Like(post=post, user=user)
        like.save()
    return redirect('SocialNetworkApp:post', post.id)

def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Проверяем, существует ли лайк для данной записи и пользователя
    like = get_object_or_404(Like, post=post, user=user)
    like.delete()
    page_url = f'post/{post_id}/'
    return redirect('SocialNetworkApp:post', post.id)



