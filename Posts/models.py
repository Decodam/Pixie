from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    """Model definition for Comment."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for Comment."""

        ordering = ['-date_posted'] 
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return f"{self.author.username}'s comment, id=> {self.id}"


class Tag(models.Model):
    """Model definition for Tag."""

    name = models.CharField(max_length=250, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for Tag."""
        ordering = ['name'] 
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name



class Post(models.Model):
    """Model definition for Post."""

    image = models.ImageField(upload_to='posts_pics')
    caption = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name="Post_tags", blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name="Post_likes", blank=True)
    hearts = models.ManyToManyField(User, related_name="Post_hearts", blank=True)
    comments = models.ManyToManyField(Comment, related_name="Post_comments", blank=True)


    class Meta:
        """Meta definition for Post."""

        ordering = ['-date_posted'] 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return f"{self.author.username}'s post, id=> {self.id}"




class Message(models.Model):
    """Model definition for Message."""
    OPTIONS = (
		('Report bugs', 'Report bugs'),
		('Report posts', 'Report posts'),
		('Report security issues', 'Report security issues'),
		('Help for projects', 'Help for projects'),
		('For business', 'For business'),
		('Others', 'Others'),
	) 

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200, null=True, choices=OPTIONS)
    message = models.TextField(max_length=400)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for Message."""

        ordering = ['-date_posted'] 
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return f"{self.name}'s message"
