from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls.base import reverse
from django.utils import timezone
from django.utils.timezone import now
from django.template.defaultfilters import slugify
GENDER_CHOICES = ( 
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
 )

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class WorkCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='blogposts')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)
    cover = models.ImageField(upload_to='images/blog')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=60)
    email = models.EmailField()
    website = models.URLField(max_length=2083, blank=True, null=True)
    content = models.TextField()
    created_on =  models.DateTimeField(default=timezone.now)
    
class Reply(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on =  models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Comment', on_delete=models.CASCADE)
    
class OurCause(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    donated_money = models.FloatField()
    raised_money = models.FloatField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    categories = models.ManyToManyField('Category', related_name='ourcauses')
    cover = models.ImageField(upload_to='images/ibikorwa')
    def __str__(self):
        return self.title   
    
    def get_absolute_url(self):
        return reverse('cause-detail', kwargs={'slug': self.slug})
    

class Event(models.Model):
    date = models.DateField(blank=False, null=False)
    title = models.CharField(max_length=255)
    time = models.TimeField(blank=False, null=False)
    avenue = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    cover = models.ImageField(upload_to='images/event')
    
    
class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    created_on =  models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name 

class Volunteer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    nationality = models.CharField(max_length=30)
    id_number = models.IntegerField(default=1)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    created_on =  models.DateTimeField(default=timezone.now)


class Program(models.Model):
    cover = models.ImageField(upload_to='images/program')
    title = models.CharField(max_length=100)
    umurenge = models.CharField(max_length=50)
    akagali = models.CharField(max_length=50)
    umudugudu = models.CharField(max_length=50)
    description = models.TextField()
    categories = models.ManyToManyField('WorkCategory', related_name='program')
    slug = models.SlugField(null=True,blank=True, unique=True)
    
  
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('program_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Abana(models.Model):
    profile_image = models.ImageField(upload_to='images/abana')
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    umurenge = models.CharField(max_length=50)
    akagali = models.CharField(max_length=50)
    umudugudu = models.CharField(max_length=50)
    igihe_yabyariye = models.DateField()
    abana_afite = models.IntegerField(default=1)
    ikiciro_ubudehe = models.CharField(max_length=1)
    afite_ubwishingizi = models.BooleanField(default=False)
    testimonials = models.TextField()
    
    
    
    
    
        
    
    


