from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from Posts.models import Post

# Create your models here.

class Notification(models.Model):
    """Model definition for Notification."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_who_is_the_author")
    content = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="user_who_is_the_target")
    target = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_who_is_the_target")
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        
        ordering = ['-date_posted'] 
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        """Unicode representation of Notification."""
        return self.content


class Profile(models.Model):
    GENDERS = (
		('male', 'male'),
		('female', 'female'),
	) 

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDERS, default="male")
    bio = models.TextField(max_length=350, blank=True, null=True)
    bookmarks = models.ManyToManyField(Post, blank=True, related_name="user_bookmarks")
    banner_pics = models.ImageField(upload_to='banner_pics', default="Banner_tnqth0.jpg")
    profile_pic = models.ImageField(upload_to='profile_pics', default="Avatar_1_d3tcxq.png")


    show_email_to_public = models.BooleanField(default=False)
    show_names_to_public = models.BooleanField(default=True)

    following = models.ManyToManyField(User, related_name='user_following', blank=True,)
    followers = models.ManyToManyField(User, related_name='user_followers', blank=True,)


    class Meta:
        ordering = ['-id']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    def __str__(self):
        return f"{self.user.username}'s Profile"


