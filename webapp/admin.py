from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }

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
