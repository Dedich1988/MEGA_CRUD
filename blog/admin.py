from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'category', 'media_type')
    list_filter = ('post_date', 'category', 'media_type')
    search_fields = ('title', 'content')
    ordering = ('-post_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'category', 'post_date', 'comments_count')
        }),
        ('Media Options', {
            'fields': ('media_type', 'image', 'video_file', 'video_url', 'audio_file', 'audio_url'),
        }),
    )

admin.site.register(BlogPost, BlogPostAdmin)

