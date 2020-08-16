from django.contrib import admin
from .models import *
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_on',]

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name','email','id_number','gender','created_on']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','email', 'created_on',]
    

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','description','author','date',]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','avenue',]

class OurCauseAdmin(admin.ModelAdmin):
    list_display = ['title','description','donated_money', 'raised_money']
    


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OurCause, OurCauseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Abana)
admin.site.register(Program)
admin.site.register(WorkCategory)







