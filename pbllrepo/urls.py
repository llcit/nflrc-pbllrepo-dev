"""pbllrepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from filebrowser.sites import site

from reposite.views import (
    HomeView,
    ProjectPrototypeCreateView, ProjectPrototypeDetailView,
    ProjectPrototypeUpdateView, ProjectPrototypeDeleteView,
    ProjectPrototypeListView, CloneProjectView,
    ProjectTaskDetailView, ProjectTaskCreateView,
    ProjectTaskUpdateView, ProjectTaskDeleteView,
    ProjectTaskListView, ProjectPrototypeDocumentView,
    FileUploadView, ProjectFileDeleteView
)

from discussions.views import DiscussionListView, DiscussionView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^prototypes/$', ProjectPrototypeListView.as_view(), name='list_prototypes'),
    url(r'^prototype/doc/(?P<pk>[-\d]+)/$', ProjectPrototypeDocumentView.as_view(), name='docview_prototype'),
    url(r'^prototype/(?P<pk>[-\d]+)/$', ProjectPrototypeDetailView.as_view(), name='view_prototype'),
    url(r'^prototype/add/$', ProjectPrototypeCreateView.as_view(), name='create_prototype'),
    url(r'^prototype/edit/(?P<pk>[-\d]+)/$', ProjectPrototypeUpdateView.as_view(), name='update_prototype'),
    url(r'^prototype/delete/(?P<pk>[-\d]+)/$', ProjectPrototypeDeleteView.as_view(), name='delete_prototype'),
    url(r'^prototype/flip/(?P<pk>[-\d]+)/$', CloneProjectView.as_view(), name='flip_prototype'),

    # url(r'^prototypes/$', ProjectPrototypeListView.as_view(), name='list_prototypes'),
    url(r'^prototype/(?P<project>[-\d]+)/task/(?P<pk>[-\d]+)/$', ProjectTaskDetailView.as_view(), name='view_task'),
    url(r'^prototype/(?P<pk>[-\d]+)/tasks/$', ProjectTaskListView.as_view(), name='view_all_tasks'),

    url(r'^prototype/(?P<project>[-\d]+)/task/add/$', ProjectTaskCreateView.as_view(), name='create_task'),
    url(r'^prototype/(?P<project>[-\d]+)/task/edit/(?P<pk>[-\d]+)/$', ProjectTaskUpdateView.as_view(), name='update_task'),
    url(r'^prototype/(?P<project>[-\d]+)/task/delete/(?P<pk>[-\d]+)/$', ProjectTaskDeleteView.as_view(), name='delete_task'),

    # url(r'^prototype/project-file-upload/(?P<project>[-\d]+)/$', ProjectFileUploadView.as_view(), name='upload_project_file'),
    # url(r'^prototype/task-file-upload/(?P<task>[-\d]+)/$', TaskFileUploadView.as_view(), name='upload_task_file'),

    url(r'^prototype/file-upload/$', FileUploadView.as_view(), name='upload_file'),
    url(r'^prototype/project-file/delete/(?P<pk>[-\d]+)/$', ProjectFileDeleteView.as_view(), name='delete_file'),

    url(r'^discussions/(?P<slug>[-\w]+)/$', DiscussionView.as_view(), name='discussion_select'),
    url(r'^discussions/$', DiscussionListView.as_view(), name='discussion'),
    url(r'^discussions/post/add/$', PostCreateView.as_view(), name='create_post'),
    url(r'^discussions/post/delete/$', PostDeleteView.as_view(), name='delete_post'),
    url(r'^discussions/post/(?P<pk>[-\w]+)/edit/$', PostUpdateView.as_view(), name='edit_post'),



    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
