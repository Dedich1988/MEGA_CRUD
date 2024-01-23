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
    path('web_beck/', web_beck, name='web_beck'),
    path('bot/', bot, name='bot'),
    path('pars/', pars, name='pars'),

    path('pricing/', pricing, name='pricing'),

    path('subscribe/', subscribe, name='subscribe'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
