from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('album/', views.album, name='album'),
    path('timeline/', views.timeline, name='timeline'),
    path('calendar/', views.calendar, name='calendar'),
    path('funding/', views.funding, name='funding'),
    path('job/', views.job, name='job'),
    path('group/', views.group, name='group'),
    path('group_feed/', views.group_feed, name='group_feed')
]