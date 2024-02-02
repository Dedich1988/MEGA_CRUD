from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.db import IntegrityError  # Импорт для обработки исключений
from .models import *
from blog.models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def send_confirmation_email(email):
    # Функция для отправки подтверждающего письма
    subject = 'Подтверждение подписки'
    message = 'Спасибо за подписку на нашу рассылку!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)


def subscribe(request):
    # Обработка запроса на подписку
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Попытка создать новую запись подписчика
                Subscriber.objects.create(email=email)
                # Отправка подтверждающего письма
                send_confirmation_email(email)
                # Перенаправление на страницу успеха
                return redirect('webapp:home')
            except IntegrityError:
                # Обработка случая, если email уже существует
                print("Этот email уже подписан.")
    else:
        form = SubscribeForm()

    return render(request, 'main/base.html', {'form': form})


def index(request):
    """
    Renders the index page.
    """
    site = Portfolio.objects.all()
    services = Service.objects.all()
    developers = Developer.objects.all()
    faqs = FAQ.objects.all()
    latest_posts = BlogPost.objects.order_by('-post_date')[:6]
    return render(request, 'webapp/index.html', {'site': site, 'developers': developers, 'services': services,'faqs': faqs, 'latest_posts': latest_posts})




def about(request):


    projects = PortfolioProject.objects.all()

    # Разбиваем проекты на страницы (по 9 проектов на страницу)
    paginator = Paginator(projects, 9)
    page = request.GET.get('page', 1)

    try:
        portfolio = paginator.page(page)
    except PageNotAnInteger:
        portfolio = paginator.page(1)
    except EmptyPage:
        portfolio = paginator.page(paginator.num_pages)

    # Создаем диапазон страниц для пагинации
    page_range = paginator.page_range

    # Текущая страница
    current_page = int(page)
    return render(request, 'webapp/about.html', {'portfolio': portfolio, 'page_range': page_range, 'current_page': current_page})

def services(request):
    """
    Renders the services page.
    """
    return render(request, 'webapp/services.html')

def faq(request):
    """
    Renders the FAQ page.
    """
    return render(request, 'webapp/faq.html')

def team(request):
    """
    Renders the team page.
    TODO: Add logic for team page processing.
    """
    return render(request, 'webapp/teams.html')

def pars(request):
    """
    Renders the testimonials page.
    TODO: Add logic for testimonials page processing.
    """
    return render(request, 'webapp/testimonial.html')

def bot(request):
    """
    Renders the testimonials page.
    TODO: Add logic for testimonials page processing.
    """
    return render(request, 'webapp/testimonial.html')

def web_beck(request):
    """
    Renders the testimonials page.
    TODO: Add logic for testimonials page processing.
    """
    return render(request, 'webapp/testimonial.html')

def pricing(request):
    """
    Renders the pricing page.
    TODO: Add logic for testimonials page processing.
    """
    return render(request, 'webapp/pricing.html')

def contact(request):
    """
    Renders the pricing page.
    TODO: Add logic for testimonials page processing.
    """
    return render(request, 'webapp/contact.html')

def portfolio_detail(request, project_id):
    # Получаем объект проекта по его ID или возвращаем 404, если проект не найден
    project = get_object_or_404(PortfolioProject, id=project_id)

    return render(request, 'webapp/portfolio_detail.html', {'project': project})