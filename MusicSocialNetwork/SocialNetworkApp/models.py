from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/')
    middle_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=255)
    birthday = models.DateField()
    sex = models.BooleanField()
    music_network = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    post_text = models.CharField(max_length=255)
    post_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField()
    photo_post = models.ImageField(upload_to='post_photos/', default='post_photos/Rap.png')

    def __str__(self):
        return f'{self.user} - {self.post_text}'

class MusicPost(models.Model):
    post_text = models.CharField(max_length=255)
    post_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField()
    audio_post = models.FileField(upload_to='music_posts/')

    def __str__(self):
        return f'{self.user} - {self.post_text}'

class Skill(models.Model):
    name = models.CharField(max_length=100)


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.CharField(max_length=255)
    comment_date = models.DateField()
    is_self = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.text_comment}'

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Chat {self.pk}'

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.pk}'