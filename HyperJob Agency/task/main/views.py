from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


class MainPage(View):
    def get(self, request):
        template_name = 'main/main_page.html'
        return render(request, template_name)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'main/signup.html'


class LoginUser(LoginView):
    redirect_authenticated_user = True
    template_name = 'main/login.html'


def home_redirect(request):
    if request.user.is_superuser:
        return redirect('/vacancy/new')
    elif not request.user.is_superuser and request.user.is_authenticated:
        return redirect('/resume/new')
    else:
        return HttpResponse()