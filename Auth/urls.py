from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Auth/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('<int:pk>/user_detail', views.user_detail, name='user_detail'),
    path('<int:pk>/follow', views.follow, name='follow'),

    path('notifications/', views.notifications, name='notifications'),
]