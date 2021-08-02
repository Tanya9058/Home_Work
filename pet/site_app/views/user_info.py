from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User

__all__ = [
    'UserInfoPage'
]


class UserInfoPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'user_info.html', context={'user': request.user})
