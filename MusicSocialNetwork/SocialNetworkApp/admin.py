from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from SocialNetworkApp.models import *

from django.contrib.admin import ModelAdmin, register

from SocialNetworkApp.models import *

@register(Comment)
class CommentAdmin(ModelAdmin):
    model = Comment

@register(Post)
class PostAdmin(ModelAdmin):
    model = Post

@register(MusicPost)
class ProfileAdmin(ModelAdmin):
    model = MusicPost

@register(Like_Post)
class LikeAdmin(ModelAdmin):
    model = Like_Post

@register(Like_Music)
class LikeMusic(ModelAdmin):
    model = Like_Music