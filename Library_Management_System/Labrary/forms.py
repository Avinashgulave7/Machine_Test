from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .models import User

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['book_name',]
        widgets={
            'book_name': forms.TextInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','password1','password2','email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('email','password')
