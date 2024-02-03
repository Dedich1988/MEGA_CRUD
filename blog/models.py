from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.models import Tag

from taggit.managers import TaggableManager






class Post(models.Model):

    tags = TaggableManager()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {Comment.name} on {Comment.post}'

# Create your models here.






class BlogPost(models.Model):
    MEDIA_CHOICES = (
        ('IMG', 'Image'),
        ('VID', 'Video'),
        ('AUD', 'Audio'),
        ('IVA', 'Image with Audio'),
        ('NON', 'None'),
    )

    title = models.CharField(max_length=200)
    content = RichTextField()
    post_date = models.DateTimeField()
    comments_count = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    media_type = models.CharField(max_length=3, choices=MEDIA_CHOICES, default='NON')

    # Media fields
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    audio_file = models.FileField(upload_to='audios/', blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Сначала сохраняем модель
        super(BlogPost, self).save(*args, **kwargs)

        # Проверяем, есть ли изображение
        if self.image:
            img = Image.open(self.image.path)

            # Изменение размера изображения
            if img.height > 150 or img.width > 300:
                output_size = (300, 150)
                img.thumbnail(output_size)

                # Сохраняем измененное изображение
                img.save(self.image.path)
    def __str__(self):
        return self.title
