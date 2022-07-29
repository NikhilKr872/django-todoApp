from ast import Del, Delete
from django.urls import path
from .views import TaskList, TaskDetail,TaskCreate,TaskUpdate,DeleteTask,UserLogin,UserRegister
from django.contrib.auth.views import LogoutView


urlpatterns=[
    
    path('login/',UserLogin.as_view(),name="login"),
    path('register/',UserRegister.as_view(),name="register"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='taskdetail'),
    path('create/',TaskCreate.as_view(),name="taskcreate"),
    path('update/<int:pk>/',TaskUpdate.as_view(),name="taskupdate"),
    path('delete/<int:pk>/',DeleteTask.as_view(),name="deletetask")
]