from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('add/',views.addBlog,name='addblog'),
    path('like/<str:pk>',views.likeBlog,name='like'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]