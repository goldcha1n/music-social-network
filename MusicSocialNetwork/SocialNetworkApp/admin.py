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