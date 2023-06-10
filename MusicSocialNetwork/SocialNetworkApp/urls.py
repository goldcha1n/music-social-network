from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('chat/<int:chat_id>/', views.chat_messages, name='chat_messages'),
    path('chat/<int:chat_id>/send-message/', views.send_message, name='send_message'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),
    path('profileCurrent/', views.current_user_profile, name='current_user_profile'),
    path('chat/', views.chat, name='chat'),
    path('addMusic/', views.add_music, name='add_music'),
    path('addPost/', views.add_post, name='add_post'),
    path('music/', views.music, name='music'),
    path('login/', auth_views.LoginView.as_view(template_name='SocialNetworkApp/login.html'), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
]
