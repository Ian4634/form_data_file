from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LessonForm
# Create your views here.
def index(request):
    submitted = False
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
        else:
            return HttpResponseRedirect('/')
    else:
        
        if 'submitted' in request.GET:
            submitted = True
            context = {
                'submitted':submitted,
            }
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html',{'submitted':submitted, 'form':LessonForm})
    