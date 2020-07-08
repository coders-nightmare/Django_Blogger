from django.urls import path
from . import views
urlpatterns = [
    path('postComment/', views.postComment, name="postComment"),
    path('', views.blogHome, name="blogHome"),
    # Api to post commnet
    path('<str:slug>/', views.blogPost, name="blogPost"),
]
