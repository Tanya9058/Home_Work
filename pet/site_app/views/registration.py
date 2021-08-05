from django.views import View
from django.contrib.auth import login, logout, authenticate
from site_app.models import CustomUser
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
            user = CustomUser.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                address=request.POST['address'],
                about=request.POST['about']
            )
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect(f'/user_page/{user.id}')
        return render(request, 'registration.html', context={'error': 'incorrect data'})

