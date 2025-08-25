from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUp(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="password",
    )
    comfirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Comfirm Password",
    )

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            'password'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("comfirm_password"):
            raise form.ValidationError("password do not match!")
        return cleaned_data 
    
class Login(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="password",
    )