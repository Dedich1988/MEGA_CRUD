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


admin.site.register(PricingPlan, MyModelAdmin)


class BannerAdminForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
        }

@admin.register(Banner)
class BanerAdmin(admin.ModelAdmin):
    form = BannerAdminForm
    list_display = ('title', 'description', 'description_two', 'image')
