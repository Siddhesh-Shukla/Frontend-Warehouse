
from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    # PostDeleteView,
    UserPostListView
)

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', PostListView.as_view(), name='home'),
    path('workspace/', views.workspace, name = "workspace"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]