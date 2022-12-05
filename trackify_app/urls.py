from django.contrib import admin
from django.urls import path, include, re_path as url
from . import views

urlpatterns = [
   path("", views.index, name='index'),
   path("users", views.users, name='users'), 
   path("approvals", views.approvals, name='approvals'), 
   path("apps", views.apps, name='apps'), 
   path("quickcheck", views.quickcheck, name='quickcheck'), 
   path("reports", views.reports, name='reports'), 
   path("screenshots", views.screenshots, name='screenshots'), 
   path("settings_projects", views.settings_projects, name='settings_projects'), 
   path("settings", views.settings, name='settings'), 
   path("teams", views.teams, name='teams'), 
   path("time_activity", views.time_activity, name='time_activity'), 
   path("todos", views.todos, name='todos'),    
   path("urls", views.urls, name='urls'), 
   path("viewedit", views.viewedit, name='viewedit'), 
   path("weekly", views.weekly, name='weekly'), 
   path("delete_user/<str:pk>", views.delete_user, name='delete_user'),  
   path("delete_project/<str:pk>", views.delete_project, name='delete_project'), 
   path("view_screenshots/<str:pk>", views.view_screenshots, name='view_screenshots'),  
   path("projects", views.projects, name='projects'),

   # API's 
   path("api/", include('api.urls'), name='api'),
   url(r'^auth/', include('djoser.urls')),
   url(r'^auth/', include('djoser.urls.jwt')),
]