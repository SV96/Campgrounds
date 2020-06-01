from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,DeleteView,CreateView
from django.views.generic.edit import UpdateView
from .models import Campground,Comment,BookCamp,Contact
from .forms import NewCampAdd
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from src.forms import CommentForm,BookCampForm
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class CampListView(ListView):
    model = Campground
    template_name = 'home.html'
    context_object_name = 'campgrounds'

class CampDetaiView(DetailView):
    model = Campground
    template_name = 'detail.html'
    context_object_name = 'post'


class CampCreateView(LoginRequiredMixin,CreateView):
    fields = ('title','description','image','amount_type','amount','location')
    model = Campground

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
         


class CampUpdateView(LoginRequiredMixin,UpdateView):
    model = Campground
    fields = '__all__'
   


class CampDeleteView(LoginRequiredMixin,DeleteView):
    model = Campground
    template_name = 'camp_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('src:post')


def campSearch(request):
    camp = Campground.objects.all()
    template_name = 'home.html'

    search_query = request.GET.get('get_camp')
    if search_query:
        campgrounds = camp.filter(Q(title__icontains=search_query) | Q(location__icontains=search_query)).distinct()
        
        context = {
            'campgrounds':campgrounds
        }
    
    else:
        messages.warning(request, 'please Enter name or location')
        context = {
            'Not found':None
        }

    return render(request, template_name,context)



@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Campground,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  
            comment.comment_user = request.user
            comment.post = post
            comment.save()
            return redirect('src:detail',pk=post.pk)
    
    else:
        form = CommentForm()
    return render(request,'comment_form.html',{'form':form})


def comment_update(request,pk):
    context ={} 
    comment = get_object_or_404(Comment,pk=pk)
    comment_user = comment.comment_user
    post_pk = comment.post.pk
    form = CommentForm(request.POST or None, instance = comment)
    if request.user == comment_user:
        if form.is_valid(): 
            form.save() 
            return redirect('src:detail',pk=post_pk)
    context["form"] = form 
    return render(request, "comment_form.html", context) 


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('src:detail',pk=post_pk)

@login_required
def book_campground(request,pk):
    post = get_object_or_404(Campground,pk=pk)
    if request.method == "POST":
        form = BookCampForm(request.POST)
        if form.is_valid():
            bookcamp = form.save(commit=False)
            bookcamp.customer = request.user
            bookcamp.camp_book = post
            bookcamp.post = post
            bookcamp.save()
            return redirect('src:detail',pk=pk)
        
    else:
        form = BookCampForm()
    return render(request,'book_form.html',{'form':form})


def contact(request):
    template_name = 'contact.html'
    contact = Contact.objects.all()
    context = {
        'contact':contact
    }
    return render(request,template_name,context)