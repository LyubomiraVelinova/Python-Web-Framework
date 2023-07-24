from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from charityapp.accounts.forms import RegisterUserForm, CustomAuthenticationForm


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context

    def form_valid(self, form):
        proceed = self.request.POST.get('proceed', False)

        if proceed == 'Proceed':
            return redirect('additional-info-page', user_type=form.cleaned_data.get('user_type'))
        else:
            # Това ни създава user-a
            result = super().form_valid(form)
            user = self.object
            login(self.request, user)
            return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = CustomAuthenticationForm


class LogoutView(auth_views.LogoutView):
    pass
