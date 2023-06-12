from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'SocialNetworkApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post, name='post'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),
    path('profileCurrent/', views.current_user_profile, name='current_user_profile'),
    path('addMusic/', views.add_music, name='add_music'),
    path('addPost/', views.add_post, name='add_post'),
    path('addProfile/', views.add_profile, name='add_profile'),
    path('music/', views.music, name='music'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
]
