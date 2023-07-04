from django.urls import path

from charity_for_future.accounts.views import login, register

urlpatterns = [
    path('login/', login, name='login-page'),
    path('signup/', register, name='signup-page'),
]
