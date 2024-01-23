from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('infinite_scroll/', infinite_scroll, name='infinite_scroll'),
    path('single_post/', single_post, name='single_post'),
    path('two_column/', two_column, name='two_column'),
    # Добавьте остальные пути здесь
]