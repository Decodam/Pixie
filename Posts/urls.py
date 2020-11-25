from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feeds/', views.feeds, name='feeds'),

    path('scream/new/', views.create_new_scream, name="create_new_scream"),
    path('scream/details/<int:pk>/', views.scream_details, name='scream_details'),
    path('scream/update/<int:pk>/', views.update_existing_scream, name='update_existing_scream'),
    path('scream/delete/<int:pk>/', views.delete_existing_scream, name='delete_existing_scream'),
    path('scream/report/<int:pk>/', views.report_post, name='report_post'),

    path('scream/add_comment_to_scream/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('scream/add_like_to_post/<int:pk>/', views.add_like_to_post, name='add_like_to_post'),
    path('scream/add_heart_to_post/<int:pk>/', views.add_heart_to_post, name='add_heart_to_post'),
    path('scream/add_scream_to_Bookmarks/<int:pk>/', views.add_scream_to_Bookmarks, name='add_scream_to_Bookmarks'),

    path('explore/', views.explore, name='explore'),
    path('explore/tag_filter/<int:pk>/', views.tag_filter, name='tag_filter'),

    path('search/users/', views.search_users, name='search_users'),
    path('search/tags/', views.search_tags, name='search_tags'),
]