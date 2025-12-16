from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from users.models import User

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    


class UserLogoutView(LogoutView):
    pass


class UserCreateView(CreateView):
    fields = ["username", "email", "first_name", "last_name", "password"]
    template_name = "users/user_create.html"
    success_url = reverse_lazy("login")
    model = User

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)
