from django.db import models
from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    birthday = models.DateField()
    social_network = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    post_text = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_post = models.ImageField(upload_to='photo_post/', default='photo_post/Rap.png')

    def __str__(self):
        return f'{self.user} - {self.post_text}'

class MusicPost(models.Model):
    post_text = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_post = models.FileField(upload_to='music_posts/')

    def __str__(self):
        return f'{self.user} - {self.post_text}'


class Comment(models.Model):
    text_comment = models.CharField(max_length=255)
    comment_date = models.DateField(auto_now_add=True)
    is_self = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.text_comment}'