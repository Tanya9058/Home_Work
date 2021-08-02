from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

__all__ = [
    'HomePage'
]


class HomePage(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'home.html', context={'user': request.user, 'count': User.objects.count()})
