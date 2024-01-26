# Generated by Django 5.0.1 on 2024-01-26 07:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('post_date', models.DateTimeField()),
                ('comments_count', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=100)),
                ('media_type', models.CharField(choices=[('IMG', 'Image'), ('VID', 'Video'), ('AUD', 'Audio'), ('IVA', 'Image with Audio'), ('NON', 'None')], default='NON', max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('audio_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
