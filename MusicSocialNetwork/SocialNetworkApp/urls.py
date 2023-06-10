from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),
    path('profileCurrent/', views.current_user_profile, name='current_user_profile'),
    path('addMusic/', views.add_music, name='add_music'),
    path('addPost/', views.add_post, name='add_post'),
    path('music/', views.music, name='music'),
    path('login/', auth_views.LoginView.as_view(template_name='SocialNetworkApp/login.html'), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
]
