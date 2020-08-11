from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.


def test_session(request):
    name = request.session.get('name')
    if name:
        request.session.flush()
        return HttpResponse(f'Welcome {name}, refresh please.')
    else:
        request.session['name'] = 'Wen'
        return HttpResponse(f'How are you? refresh please.')


@login_required(login_url='session_learning:login')
def index(request):
    name = request.user.username
    return HttpResponse(f'Welcome {name}!')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # get user from model
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('session_learning:index')
        request.session['error_msg'] = 'username or password incorrect.'
    error_msg = request.session.pop('error_msg', default=None)
    return render(request, 'session_learning/login.html', context=dict(error_msg=error_msg))


def logout(request):
    auth.logout(request)
    return redirect('session_learning:login')
