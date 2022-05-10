from django import forms

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=50)
    email=forms.EmailField(label='Email', required=True)
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
