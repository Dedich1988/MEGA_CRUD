from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def single_post(request):
    return render(request, 'blog/single-post.html')


def infinite_scroll(request):
    return render(request, 'blog/infinite-scroll.html')


def two_column(request):
    return render(request, 'blog/two-column.html')


def load_more(request):
    return render(request, 'blog/load-more.html')


def one_column(request):
    return render(request, 'blog/one-column.html')


def three_column(request):
    return render(request, 'blog/three-column.html')


def three_column_sidebar(request):
    return render(request, 'blog/three-colum-sidbar.html')


def four_column(request):
    return render(request, 'blog/four-column.html')


def six_column_full_width(request):
    return render(request, 'blog/six-colum-full-wide.html')


# views.py post list


def post_list(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog/three-colum-sidbar.html', {'posts': posts})


# views.py в вашем приложении блога


def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/single-post.html', {'post': post})
