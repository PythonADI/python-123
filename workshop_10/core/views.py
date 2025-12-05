from django.shortcuts import render
from core.models import Post


def home_view(request):
    return render(
        request, 
        "index.html",
        {
            "posts": Post.objects.all()
        }
    )


def about_view(request):
    return render(
        request,
        "about.html"
    )
