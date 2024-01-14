from django.db import models
from ckeditor.fields import RichTextField

# Подписчики
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Прайс-планы главная страница
class PricingPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_description = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='pricing_plans/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Баннер на base.html
class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    description_two = RichTextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title

# Портфолио мини на главную
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')
    alt_text = models.CharField(max_length=255, blank=True)
    link = models.URLField(default='https://github.com/Dedich1988')  # Добавление поля link

    def __str__(self):
        return self.alt_text or "Portfolio Item"


# Портфолио мини на главную
class Developer(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = RichTextField()
    image = models.ImageField(upload_to='developers/')
    facebook_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.name