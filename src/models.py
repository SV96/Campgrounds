from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

rent_type = {
    ("day", "day"),
    ("week", "week")
}

class Campground(models.Model):
     user = models.ForeignKey(User, related_name="posts", null=True, on_delete=models.SET_NULL)
     title = models.CharField(max_length=20)
     description = models.TextField(max_length=100)
     amount_type = models.CharField(choices=rent_type, max_length=10)
     amount = models.IntegerField(default=0000)
     created_date_post = models.DateField(default=timezone.now,null=True,blank=True)
     location = models.CharField(max_length=25,null=True,blank=True)
     image = models.ImageField()

     def __str__(self):
         return self.title
        
     def get_absolute_url(self):
        return reverse('src:post') 

class Comment(models.Model):
    post = models.ForeignKey(Campground,related_name='comments',null=True,on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, related_name="commentor", null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date_comment = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('src:post')

    def __str__(self):
        return self.text

class Contact(models.Model):
    email = models.EmailField(blank=True,null=True)
    contact = models.IntegerField(default=0000,blank=True,null=True)

    def __str__(self):
         return self.email
        
class BookCamp(models.Model):
    customer = models.ForeignKey(User, related_name="customer", null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True,null=True)
    contact = models.IntegerField(default=0000,blank=True,null=True)
    camp_book = models.ForeignKey(Campground, related_name="reserve", null=True, on_delete=models.SET_NULL)
    time = models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
         return self.customer.username
        
    def get_absolute_url(self):
        return reverse('src:post') 

