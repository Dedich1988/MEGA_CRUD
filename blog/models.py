from django.db import models
from ckeditor.fields import RichTextField

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

    def __str__(self):
        return self.title
