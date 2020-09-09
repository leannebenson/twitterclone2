from django import forms
from twitteruser.models import TwitterUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
