# Generated by Django 5.0.1 on 2024-01-06 16:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_pricingplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingplan',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
