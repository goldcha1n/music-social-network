from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'SocialNetworkApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post, name='post'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('post/like/<int:post_id>', views.like_post, name='like_post'),
    path('post/unlike/<int:post_id>', views.unlike_post, name='unlike_post'),
    path('liked_posts/', views.liked_posts, name='liked_posts'),
    path('music/', views.music, name='music'),
    path('music/<int:music_id>/delete', views.delete_music, name='delete_music'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),
    path('profileCurrent/', views.current_user_profile, name='current_user_profile'),
    path('addMusic/', views.add_music, name='add_music'),
    path('addPost/', views.add_post, name='add_post'),
    path('addProfile/', views.add_profile, name='add_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
]
