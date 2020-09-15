from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from authentication.forms import SignUpForm, LoginForm
from django.views.generic import TemplateView

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})



# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, username=data.get(
#                 "username"), password=data.get("password"))
#             if user:
#                 login(request, user)
#                 # return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
#                 return HttpResponseRedirect(reverse("homepage"))
#     form = LoginForm()
#     return render(request, "generic_form.html", {"form": form})


class LoginView(TemplateView):
    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage')) 
            else:
                form = LoginForm()
                return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
