from django.contrib import admin
from django.urls import path
from main.views import *
from resume.views import *
from vacancy.views import *
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('resumes/', ResumesPage.as_view()),
    path('vacancies/', VacanciesPage.as_view()),
    path('login', LoginUser.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', SignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('vacancy/new', create_vacancy),
    path('resume/new', create_resume),
    path('home/', home_redirect)
]
