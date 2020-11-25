from django.contrib import admin
from .models import Profile, Notification

# Register your models here.

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_pic')
    search_fields = ('user__username', 'user__email')

admin.site.register(Notification)