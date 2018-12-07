from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', required=True,
                               widget=forms.TextInput(
                                attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', required=True, 
                             widget=forms.EmailInput(
                              attrs={"class": 'form-control'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={
                                'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',  
                                widget=forms.PasswordInput(attrs={
                                 'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("This username is already registered.")
        return username
        

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, 
                               widget=forms.TextInput(
                                attrs={"class": 'form-control'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={
                                'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm, self).clean(*args, **kwargs)
