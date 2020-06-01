from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'src'

urlpatterns = [
  path('',views.CampListView.as_view(),name='post'),
  path('campgrounds/<int:pk>',views.CampDetaiView.as_view(),name='detail'),
  path('campgrounds/new',views.CampCreateView.as_view(),name='new'),
  path('campgrounds/edit/<int:pk>',views.CampUpdateView.as_view(template_name='camp_update.html'),name='update'),
  path('campgrounds/delete/<int:pk>',views.CampDeleteView.as_view(),name='remove'),
  path('campgrounds/search/',views.campSearch,name='search'),
  path('campgrounds/<int:pk>/comment',views.add_comment_to_post,name='add_comment'),
  path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
  path('comment/<int:pk>/edit/', views.comment_update, name='comment_update'),
  path('campgrounds/<int:pk>/book/',views.book_campground,name='reserve'),
  path('campgrounds/contatc_us/',views.contact,name='contact_us'),

]
