from django.urls import path

from core.views import (
    home_view,
    about_view,
    post_details_view,
    post_create_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("post/add/", post_create_view, name="post_add"),
    path("post/<int:pk>/", post_details_view, name="post_details"),
    path("about/", about_view, name="about"),
]
