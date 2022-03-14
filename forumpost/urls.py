from django.urls import path

from .views import *

app_name = 'forumpost'

urlpatterns = [
    path('post_view/<int:id>', forum_post_view,name='forum-post-view'),
    path('forum/', forum_page_view,name='forum-page-view'),
    path('forumdetail/', forum_detail_view,name='forum-detail-view'),

    
]
