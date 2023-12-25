from django.urls import path

from MyApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('userhome',views.userhome,name='userhome'),
    path('addtask',views.addtask,name='addtask'),
    path('viewtask',views.viewtask,name='viewtask'),
    path('taskupdate/<int:id>/',views.taskupdate,name='taskupdate'),
    path('taskdelete/<int:id>/',views.taskdelete,name='taskdelete'),

    ]