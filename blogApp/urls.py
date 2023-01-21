from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # path('', include('blogApp.urls')),
    path('get-blog/<id>/', get_blog),
    path('',home),
    path('login/', mylogin , name="myLogin"),
    path('logout/', myLogout , name="myLogout"),
    
    path('register/', myregister, name="register"),
    path('showAllBlogs/', showAllBlogs, name="showAllBlogs"),
    path('createBlog/', createBlog, name="createBlog"),
    path('updateBlog/<id>/', updateBlog, name="updateBlog"),
    path('deleteBlog/<id>/', deleteBlog, name="deleteBlog"),
    
    
]
