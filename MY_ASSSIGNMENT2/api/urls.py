from django.urls import path
from .views import (
    PostListCreateView,
    PostLikeView,
    PostShareView,
    PostCommentView,
    RetrieveView
)

urlpatterns = [
    path('postscreate/', PostListCreateView.as_view(), name='post-list-create'),
    
    path(' ', RetrieveView.as_view(), name='post-retrieve-update-destroy'),
    path('postlist/', RetrieveView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/share/', PostShareView.as_view(), name='post-share'),
    path('posts/<int:pk>/comment/', PostCommentView.as_view(), name='post-comment'),
    path('posts/<int:pk>/', RetrieveView.as_view(), name='post-view')
]
