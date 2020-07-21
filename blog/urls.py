from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from .import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name="blog-detail"),
    path("post/new/", PostCreateView.as_view(), name="blog-new"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(), name="blog-update"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(), name="blog-delete"),
    path('about/',views.about,name='blog-about'),




]
