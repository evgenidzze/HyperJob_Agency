from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden
from .forms import ResumeForm
from .models import Resume


class ResumesPage(View):
    def get(self, request):
        template_name = 'resume/resumes.html'
        resume = Resume.objects.all()
        context = {'resume': resume}
        return render(request, template_name, context=context)


def create_resume(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ResumeForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                Resume.objects.create(description=form['description'], author=request.user)
                return redirect('/')
        form = ResumeForm
        data = {
            'form': form
        }
    else:
        return HttpResponseForbidden(status=403)
    return render(request, 'resume/create_resume.html', data)
