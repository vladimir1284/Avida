from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    from django import forms    


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Usuario',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )