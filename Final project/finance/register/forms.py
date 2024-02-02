from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from accounts.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control mx-auto w-auto mb-3', 'placeholder': 'Email'}),
        label="",
    )

    username = UsernameField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control mx-auto w-auto mb-3', 'placeholder': 'Username'}),
        label="",
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mx-auto w-auto mb-3', 'placeholder': 'Password'}),
        label="",
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mx-auto w-auto mb-3', 'placeholder': 'Confirm Password'}),
        label="",
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mx-auto w-auto mb-3',
                'placeholder': 'Username',
            }
        ),
        label=""
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mx-auto w-auto mb-3',
                'placeHolder': 'Password'
            }
        ),
        label=""
    )
