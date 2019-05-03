from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    print('1')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, ('You have been logged in'))
            return redirect('students')

        else:
            messages.success(request, ('Your username or password is invalid'))
            return redirect('home')

    else:
         return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("You've been registered..."))
            return redirect('home')
    else:
        form=UserCreationForm

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def logout_user(request):
    auth.logout(request)
    messages.success(request, ('You have been logged out...'))
    return  redirect('home')
