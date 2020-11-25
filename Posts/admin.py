from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('id', 'author', 'image', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('author__username', 'id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('id', 'author', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('author__username', 'id')


admin.site.register(Tag)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    '''Admin View for Message'''

    list_display = ('name', 'email', 'subject')
    list_filter = ('date_posted', 'subject')
    search_fields = ('name', 'email')