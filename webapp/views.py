from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'webapp/index.html')

def about(request):

    return render(request, 'webapp/about.html')

def services(request):

    return render(request, 'webapp/services.html')

def faq(request):

    return render(request, 'webapp/faq.html')

def team(request):
    # Ваш код для обработки страницы команды
    return render(request, 'webapp/teams.html')

def testimonials(request):
    # Ваш код для обработки страницы отзывов
    return render(request, 'webapp/testimonial.html')

