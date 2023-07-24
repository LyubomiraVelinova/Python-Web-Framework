from django.urls import path, include

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView

# AdditionalRegisterUserInfoView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-page'),
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout-page'),
]
