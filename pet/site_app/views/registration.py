from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .auth import Login

__all__ = [
    'Registration',
]


class Registration(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'registration.html')
        return redirect('/user_page')

    def post(self, request):
        if request.POST['password'] == request.POST['check_password']:
            user = User.objects.create(
                username=request.POST['username'],
            )
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('/user_page/')
        return render(request, 'registration.html', context={'error': 'incorrect data'})