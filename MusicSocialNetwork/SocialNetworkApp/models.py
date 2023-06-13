from django.db import models
from users.models import User


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


class Like_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.post_text}"


class Like_Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(MusicPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.music.post_text}"