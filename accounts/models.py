from django.db import models
from django.contrib import auth
from django.utils import timezone
from src.models import Campground,Comment
from django.contrib.auth import get_user_model
info = get_user_model()
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}" .format(self.username)


class userProfile(models.Model):
    user = models.ForeignKey(info, related_name="info", null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100,default='user')
    last_name = models.CharField(max_length=100,default='user')
    date_of_birth = models.DateField()
    about = models.TextField(max_length=100)
    visited_Place = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to = 'profile')

    def __str__(self):
        return self.user.username