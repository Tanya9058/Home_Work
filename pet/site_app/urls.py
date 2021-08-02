from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view()),

    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('registration/', Registration.as_view()),

    path('user_page/', UserPage.as_view()),
    path('home/', HomePage.as_view()),
    path('contacts/', ContactsPage.as_view()),
    path('user_info/', UserInfoPage.as_view())
]
