from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from charityapp.accounts.forms import RegisterUserForm


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home-page')

    # When register to login automatically - NOT WORKING
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object

        login(self.request, user)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutView(auth_views.LogoutView):
    pass
