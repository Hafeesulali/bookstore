from django.shortcuts import render, redirect
from book.models import Books
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from customer.forms import UserRegistrationForm, LoginForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
class CustomerIndex(ListView):
    model = Books
    template_name = "customer_home.html"
    context_object_name = "books"


# class CustomerIndex(View):
#     def get(self, request, *args, **kwargs):
#         qs = Books.objects.all()
#         return render(request, "customer_home.html", {"books": qs})


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("sign in")


# class SignUpView(View):
#     def get(self, request, *args, **kwargs):
#         form = UserRegistrationForm()
#         return render(request, "signup.html", {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("sign in")
#         else:
#             return render(request, "signup.html", {"form": form})


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "signin.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                print("login success")
                login(request, user)
                return redirect("custhome")
            else:
                print("login failed")
                return render(request, "signin.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("sign in")


class PasswordReset(View):
    def get(self, request, *args, **kwargs):
        form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get("old_password")
            new_password = form.cleaned_data.get("new_password")
            user = authenticate(request, username=request.user, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect("sign in")
            else:
                return render(request, "password_reset.html", {"form": form})
        else:
            return render(request, "password_reset.html", {"form": form})
