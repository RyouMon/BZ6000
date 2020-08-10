from io import BytesIO

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from common.captcha.letters import gen_code
# Create your views here.


@login_required(login_url='captcha_learning:login')
def index(request):
    return render(request, 'captcha_learning/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        code = request.POST['verify_code']
        user = auth.authenticate(username=username, password=password)

        # code required
        if not code:
            request.session['msg'] = 'verify code required.'
            return redirect('captcha_learning:login')

        # code verify
        if code == request.session.get('verify_code'):

            # user verify
            if user:
                auth.login(request, user)
                return redirect('captcha_learning:index')
            # user verify failed
            request.session['msg'] = 'Username of password incorrect.'
            return redirect('captcha_learning:login')

        # code verify failed
        request.session['msg'] = 'verify code incorrect.'
        return redirect('captcha_learning:login')

    # GET
    msg = request.session.pop('msg', None)
    return render(request, 'captcha_learning/login.html', {'msg': msg})


def captcha_img(request):
    stream = BytesIO()
    img, code = gen_code()
    img.save(stream, 'PNG')
    request.session['verify_code'] = code
    return HttpResponse(stream.getvalue())
