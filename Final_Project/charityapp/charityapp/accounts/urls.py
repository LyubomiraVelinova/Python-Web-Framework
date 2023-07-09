from django.urls import path

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='signup-user-page'),
    path('login/', LoginUserView.as_view(), name='login-user-page'),
    path('logout/', LogoutView.as_view(), name='logout-user-page'),
]
