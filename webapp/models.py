from django.db import models
from ckeditor.fields import RichTextField

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class PricingPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_description = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='pricing_plans/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    description_two = RichTextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title
