from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from core.models import Post
from core.forms import PostCreateForm


def home_view(request: HttpRequest) -> HttpResponse:
    return render(
        request, 
        "index.html",
        {
            "posts": Post.objects.all().order_by("-create_date")
        }
    )


def post_details_view(request: HttpRequest, pk: int) -> HttpResponse:
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exists!")

    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "post_details.html",
        {
            "post": post
        }
    )

@login_required
def post_create_view(request: HttpRequest) -> HttpResponse:
    # if not request.user.is_authenticated:
    #     return redirect("home")
    print(request.method)
    print(request.POST)
    print(request.user)
    if request.method == "POST":
        # This is when user send filled form data!
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
        return render(
            request,
            "post_create.html",
            {
                "form": form
            }
        )

    # this is when user enter page for the first time!
    form = PostCreateForm()
    return render(
        request,
        "post_create.html",
        {
            "form": form
        }
    )


def about_view(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "about.html"
    )
