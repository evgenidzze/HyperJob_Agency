from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from .forms import VacancyForm
from django.http import HttpResponseForbidden


class VacanciesPage(View):
    def get(self, request):
        template_name = 'vacancy/vacancies.html'
        vacancy = Vacancy.objects.all()
        return render(request, template_name, {'vacancy': vacancy})


def create_vacancy(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = VacancyForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                Vacancy.objects.create(description=form['description'], author=request.user)
                return redirect('/')
        form = VacancyForm
        data = {
            'form': form
        }
    else:
        return HttpResponseForbidden(status=403)
    return render(request, 'vacancy/create_vacancy.html', data)
