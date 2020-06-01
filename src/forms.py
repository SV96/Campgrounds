from django import forms
from .models import Campground,Comment,BookCamp
from django.utils import timezone




class NewCampAdd(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description'}))
    amount_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    created_date_post = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    image = forms.ImageField()
    class Meta:   
        model = Campground
        fields = ('title','description','image','amount_type','amount','location')
       
   
class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comment'}))
    class Meta():
        model = Comment
        fields = ('text',)
        exclude = ["comment_user"]


class BookCampForm(forms.ModelForm):
    class Meta():
        model = BookCamp
        fields = ('email','contact','time')
        exclude = ["customer","camp_book"]

        