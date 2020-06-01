from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import userProfile

class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    class Meta:
        fields = ('username','email','password','password2')
        model = get_user_model()

class userProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last_name'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    about = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'about'}))
    visited_Place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'visited_Place'}))
    user_image = forms.ImageField()
    class Meta:
        model = userProfile
        fields = ('first_name','last_name','date_of_birth','about','visited_Place','user_image')
        exclude = ["user"]