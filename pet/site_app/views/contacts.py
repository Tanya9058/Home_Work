from django.views import View
from django.shortcuts import render, redirect
from site_app.models import Contact

__all__ = [
    'ContactsPage'
]


class ContactsPage(View):
    def get(self, request):
        return render(request, 'contacts.html', context={'contact': Contact.objects.all()[0]})

