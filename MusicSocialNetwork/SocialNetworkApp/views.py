from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def chat(request):
    user_chats = Chat.objects.filter(participants=request.user)
    return render(request, 'SocialNetworkApp/chat.html', {'user_chats': user_chats})

def chat_messages(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all()
    return render(request, 'SocialNetworkApp/chat_messages.html', {'chat': chat, 'messages': messages})

def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        text = request.POST['message']
        message = Message.objects.create(chat=chat, sender=request.user, text=text)
        return redirect('chat_messages', chat_id=chat_id)
    return render(request, 'SocialNetworkApp/send_message.html', {'chat': chat})



class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_text', 'post_date', 'photo_post']


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'SocialNetworkApp/addPost.html', {'form': form})


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
    print('user : c'+user)
    posts = Post.objects.select_related('user__profile').filter(user=user)
    return render(request, 'SocialNetworkApp/profile_user.html', {'user': user, 'posts': posts})




def chat(request):
    return render(request, 'SocialNetworkApp/chat.html')

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
            return redirect('home')
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
            return redirect('home')
        else:
            # Обработка ошибки неверных данных авторизации
            pass
    return render(request, 'SocialNetworkApp/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def add_post(request):
    return render(request, 'SocialNetworkApp/addPost.html')

def add_music(request):
    return render(request, 'SocialNetworkApp/addMusic.html')

class CreateChatForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = ['participants']


def chat(request):
    user_chats = Chat.objects.filter(participants=request.user)

    if request.method == 'POST':
        form = CreateChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.save()
            chat.participants.add(request.user)
            return redirect('chat_messages', chat_id=chat.id)
    else:
        form = CreateChatForm()

    return render(request, 'SocialNetworkApp/chat.html', {'user_chats': user_chats, 'form': form})