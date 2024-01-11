# webapp/context_processors.py

from .models import Banner

def banner_context(request):
    banners = Banner.objects.all()
    return {'banners': banners}
