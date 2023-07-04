from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
    )
    email = forms.CharField(
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class SignUpForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Volunteer'),
        (2, 'Member of the club'),
        (3, 'Sponsor'),
        (4, 'Admin')
    )

    first_name = forms.CharField(
        max_length=25,
    )
    last_name = forms.CharField(
        max_length=25,
    )
    email = forms.CharField(
        widget=forms.EmailInput()
    )
    phone_number = forms.IntegerField(
        required=False,
    )
    volunteer = forms.ChoiceField(
        choices=OCCUPANCIES,
    )
