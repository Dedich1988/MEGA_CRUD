# Generated by Django 5.0.1 on 2024-01-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='link',
            field=models.URLField(default='https://github.com/Dedich1988'),
        ),
    ]
