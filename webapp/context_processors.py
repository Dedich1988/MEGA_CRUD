# webapp/context_processors.py

from .models import Banner, PricingPlan

def banner_context(request):
    banners = Banner.objects.all()
    return {'banners': banners}


def PricingPlan_context(request):
    plans = PricingPlan.objects.all()
    return {'plans': plans}

