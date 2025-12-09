from django.shortcuts import render
from core.models import Post


def home_view(request):
    return render(
        request, 
        "index.html",
        {
            "posts": Post.objects.all().order_by("-create_date")
        }
    )


def about_view(request):
    return render(
        request,
        "about.html"
    )
