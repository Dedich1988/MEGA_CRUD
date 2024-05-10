from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('infinite_scroll/', infinite_scroll, name='infinite_scroll'),
    path('single_post/', single_post, name='single_post'),
    path('two_column/', two_column, name='two_column'),
    path('load_more/', load_more, name='load_more'),
    path('one_column/', one_column, name='one_column'),
    path('three_column/', three_column, name='three_column'),
    path('three_column_sidebar/', three_column_sidebar, name='three_column_sidebar'),
    path('four_column/', four_column, name='four_column'),
    path('six_column_full_width/', six_column_full_width, name='six_column_full_width'),
    # Добавьте остальные пути здесь

    #CRUD постов блога
    path('', post_list, name='post_list'),  # Список всех постов
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Детали отдельного поста
    # path('post/new/', views.post_create, name='post_create'),  # Создание нового поста
    # path('post/<int:pk>/edit/', views.post_update, name='post_update'),  # Обновление поста
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # Удаление поста
]
