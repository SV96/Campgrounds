from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from src.models import Campground
from accounts.models import userProfile
from . import forms
from .forms import userProfileForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def userProfileCreate(request,pk):
   
    if request.method == "POST":
        form = userProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('src:detail',pk=pk)
    
    else:
        form = userProfileForm()
    return render(request,'userprofile_form.html',{'form':form})


def userProfileShow(request,pk):
    post = Campground.objects.all().filter(user=request.user)
    info = userProfile.objects.all().filter(user=request.user)
    template_name= 'user_detail.html'
    context = {
        'post':post,
        'info':info,
       
    }
    return render(request,template_name,context)

def userInfoEdit(request,pk):
    info = userProfile.objects.filter(user=request.user).first()
    context = {}
    
    form = userProfileForm(request.POST or None,instance=info)
    if form.is_valid():
        form.save()
        return redirect('src:post')
    context["form"] = form
    return render(request,'userprofile_form.html',context)

