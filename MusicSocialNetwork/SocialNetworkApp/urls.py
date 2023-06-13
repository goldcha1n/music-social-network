from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'SocialNetworkApp'

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Posts
    path('addPost/', views.add_post, name='add_post'),
    path('post/<int:post_id>', views.post, name='post'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('post/like/<int:post_id>', views.like_post, name='like_post'),
    path('post/unlike/<int:post_id>', views.unlike_post, name='unlike_post'),
    path('liked_posts/', views.liked_posts, name='liked_posts'),
    # Music
    path('addMusic/', views.add_music, name='add_music'),
    path('music_post/<int:music_id>', views.music_post, name='music_post'),
    path('music/like/<int:music_id>', views.like_music, name='like_music'),
    path('music/unlike/<int:music_id>', views.unlike_music, name='unlike_music'),
    path('music/', views.music, name='music'),
    path('music/<int:music_id>/delete', views.delete_music, name='delete_music'),
    path('liked_musics/', views.liked_musics, name='liked_musics'),
    # Profile
    path('addProfile/', views.add_profile, name='add_profile'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),
    path('profileCurrent/', views.current_user_profile, name='current_user_profile'),
]
