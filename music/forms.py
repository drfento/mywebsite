from django.contrib.auth.models import User
from django import forms

# override user form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # info about class
    class Meta:
        model = User
        fields = ['username','email','password']
