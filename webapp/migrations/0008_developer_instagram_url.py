# Generated by Django 5.0.1 on 2024-01-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
    ]
