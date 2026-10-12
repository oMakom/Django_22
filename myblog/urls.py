from django.urls import path
from myblog.apps import MyblogConfig
from .views import PostsListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = MyblogConfig.name

urlpatterns = [
    path('blogs/', PostsListView.as_view(), name='posts_list'),
    path('blogs/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blogs/new/', PostCreateView.as_view(), name='post_create'),
    path('blogs/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('blogs/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
