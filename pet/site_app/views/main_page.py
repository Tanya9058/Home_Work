from django.views import View
from django.shortcuts import render, redirect

__all__ = [
    'MainPage',
]


class MainPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/user_page/')
        return render(request, 'index.html')
