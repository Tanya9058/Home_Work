from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

__all__ = [
    'Login',
    'Logout',
]


class Login(View):
    def post(self, request):
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(f'/user_page/{request.user.id}')
        else:
            return render(request, 'index.html', context={'error': 'incorrect data'})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
