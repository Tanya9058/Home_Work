from django.views import View
from django.shortcuts import render, redirect
from site_app.models import CustomUser

__all__ = [
    'UserPage',
]


class UserPage(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            return render(request, 'user_page.html', context={'user': CustomUser.objects.get(id=user_id)})
        return redirect('/')
