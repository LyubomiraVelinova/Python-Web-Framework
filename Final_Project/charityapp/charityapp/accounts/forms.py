from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    # user_type = forms.ChoiceField(choices=UserType.choices())
    # proceed = forms.BooleanField(widget=forms.HiddenInput(), initial=False)

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'user_type')


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'EMAIL'
        self.fields['password'].widget.attrs['placeholder'] = 'PASSWORD'

