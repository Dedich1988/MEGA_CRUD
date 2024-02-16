# Generated by Django 5.0.1 on 2024-02-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('completed_date', models.DateField()),
                ('image', models.ImageField(upload_to='portfolio_images/')),
            ],
        ),
    ]
