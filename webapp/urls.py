from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('faq/', faq, name='faq'),
    path('team/', team, name='team'),
    path('testimonials/', testimonials, name='testimonials'),
    path('subscribe/', subscribe, name='subscribe'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
