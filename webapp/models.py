from django.db import models
from ckeditor.fields import RichTextField

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


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


# Разработчики
class Developer(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = RichTextField()
    image = models.ImageField(upload_to='developers/')
    facebook_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


# Услуги кратко на главную страницу
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")
    url = models.URLField(verbose_name="Ссылка на страницу услуги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сначала сохраняем модель

        if self.image:
            # Открытие изображения
            pil_image = Image.open(self.image)

            # Проверяем, необходимо ли изменять размер
            if pil_image.width > 290 or pil_image.height > 200:
                output_size = (290, 200)
                pil_image = pil_image.resize(output_size, Image.LANCZOS)

                # Сохранение измененного изображения
                temp_file = BytesIO()
                pil_image.save(temp_file, format='JPEG')
                temp_file.seek(0)

                self.image.save(self.image.name, ContentFile(temp_file.read()), save=False)
                temp_file.close()


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# Проекты портфолио
class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    completed_date = models.DateField()
    image = models.ImageField(upload_to='portfolio_images/')

    def save(self, *args, **kwargs):
        # Вызываем оригинальный метод save
        super().save(*args, **kwargs)

        # Проверяем, есть ли изображение
        if self.image:
            # Открываем изображение с помощью Pillow
            img = Image.open(self.image.path)

            # Устанавливаем новый размер
            new_size = (350, 263)
            img = img.resize(new_size)

            # Перезаписываем изображение
            buffer = BytesIO()
            img.save(buffer, format='JPEG')

            # Сохраняем перезаписанное изображение
            file_name = f"{self.image.name.split('.')[0]}_resized.jpg"
            file_content = ContentFile(buffer.getvalue())
            self.image.save(file_name, file_content, save=False)

            # Сохраняем модель с обновленным изображением
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# Сообщения контактов
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# Отзывы
class Review(models.Model):
    name = models.CharField(max_length=100)  # Имя пользователя
    profession = models.CharField(max_length=100)  # Профессия пользователя
    message = models.CharField(max_length=100)  # Сообщение
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Количество звезд от 1 до 5
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)  # Поле для изображения

    def __str__(self):
        return f"{self.name} - {self.stars} stars"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сначала сохраняем модель

        if self.image:
            # Открываем изображение с помощью PIL
            img = Image.open(self.image.path)

            # Подгоняем изображение под размер 100x100
            img_resized = img.resize((100, 100), Image.LANCZOS)

            # Перезаписываем изображение
            img_resized.save(self.image.path)
