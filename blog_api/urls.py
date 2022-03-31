from django.contrib import admin
from django.urls import path,include
from .import views


app_name='blog_api'
urlpatterns = [
    path('categories/',views.CategoryList.as_view(),name='Categories'),
    path('category/<int:pk>',views.CategoryDetail.as_view(),name='category'),
    
    path('posts/',views.PostList.as_view(),name='posts'),
    path('post/<int:pk>',views.PostDetail.as_view(),name='post'),
    
    path('comments/',views.CommentList.as_view(),name='comments'),


    path('users/',views.UserList.as_view(),name='users'),
    path('user/<int:pk>',views.UserDetail.as_view(),name='user'),
]
