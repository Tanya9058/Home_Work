from django.views import View
from django.shortcuts import render, redirect

__all__ = [
    'UserPage',
]


class UserPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'user_page.html', context={'name': request.user.username})
        return redirect('/')
