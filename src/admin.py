from django.contrib import admin
from .models import Campground,Comment,BookCamp,Contact
# Register your models here.

class CampgroundAdmin(admin.ModelAdmin):
    list_display = ['user','title','amount','amount_type','created_date_post','location']
    search_fields = ['title', 'amount']      
    list_filter = ['amount_type', 'created_date_post']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_user','text','created_date_comment']
    list_filter = ['comment_user']


class BookCmapAdmin(admin.ModelAdmin):
    list_display = ['customer','contact','time','camp_book']
    search_fields = ['customer','camp_book','contact']
    list_filter = ['customer','camp_book']


admin.site.register(Campground, CampgroundAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(BookCamp,BookCmapAdmin)
admin.site.register(Contact)


