from django.contrib import admin

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},

    }
    ordering = 'pk', # Фильтры для админки
    search_fields = 'pk','title' # Настройка поиска под каждую модель нужно смотреть поля

@admin.register(ContactMessage) # Отоброжение контактной формы в административной панели
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = "name", "subject", "email"

admin.site.register(Review, MyModelAdmin)

admin.site.register(PortfolioProject, MyModelAdmin)

# Регистрация модели PricingPlan с использованием MyModelAdmin
admin.site.register(PricingPlan, MyModelAdmin)

# Регистрация модели Portfolio с использованием MyModelAdmin
admin.site.register(Portfolio, MyModelAdmin)

# Регистрация модели Portfolio с использованием MyModelAdmin
admin.site.register(Banner, MyModelAdmin)

# Регистрация модели Developer с использованием MyModelAdmin
admin.site.register(Developer, MyModelAdmin)

# Регистрация модели Service с использованием MyModelAdmin
admin.site.register(Service, MyModelAdmin)

# Регистрация модели FAQ с использованием MyModelAdmin
admin.site.register(FAQ, MyModelAdmin)
