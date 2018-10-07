from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Hello World")

    return render(request, 'LandingPage/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'LandingPage/index.html', args)