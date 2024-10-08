from django.db import models
from account.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.conf import settings
import uuid


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachment')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='post_attachment', on_delete=models.CASCADE)

class Specialty(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def natural_key(self):
        return (self.name)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Specialties'


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    specialty = models.ManyToManyField(Specialty, blank=True)
    image = models.ImageField(upload_to='doctor', null=True, blank=True)
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()

    def natural_key(self):
        return (self.name)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_thumbnails(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'https://picsum.photos/200/200'

   
 
    def __str__(self):
        return self.name


class Reserve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    attachment = models.ManyToManyField(PostAttachment, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    specialty = models.ManyToManyField(Specialty, blank=True)
    doctor = models.ManyToManyField(Doctor)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.body
    
    def save(self, *args, **kwargs):
        value = self.body
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Date(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    date_at = models.DateTimeField(blank=True, null=True)
    doctor = models.ManyToManyField(Doctor)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-date_at',)

    def __str__(self):
        return self.name


class Services(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    thumbnails = models.ImageField(upload_to='services', blank=True, null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_thumbnails(self):
        if self.thumbnails:
            return settings.WEBSITE_URL + self.thumbnails.url
        else:
            return 'https://picsum.photos/200/200'

    def __str__(self):
        return self.title





