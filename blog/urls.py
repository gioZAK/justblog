from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
