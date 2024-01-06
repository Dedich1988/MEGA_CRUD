from django.contrib import admin
from .models import PricingPlan
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }

admin.site.register(PricingPlan, MyModelAdmin)
