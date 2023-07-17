from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages

from .forms import CreateUserForm

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

    context = {'form': form}
    return render(request, 'register.html', context)


def session(request):
    ...


def dashboard(request):
    ...