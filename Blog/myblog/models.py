from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import date, datetime
# Create your models here.

# side note, when making changes to models.py make sure to makemigrations and then migrate. Even if you just changed the name of a model. Also if your adding a new model make sure to include it in the admin.py file so you can see it in the admin page.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # returns you to home page when you edit or post anything
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(default={'cols': 80, 'rows': 30})
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    # likes = models.ManyToManyField(User, related_name='blog_post')
    snippet = models.CharField(
        max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        # returns you to home page when you edit or post anything
        return reverse('home')
