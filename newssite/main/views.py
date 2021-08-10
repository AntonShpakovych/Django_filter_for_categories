from main.models import News, Category
from django.http.response import HttpResponse
from django.shortcuts import render
from main import *


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Список новостей',
        'news': news,
        'categories': categories
    }
    return render(request, 'main/home_page.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    return render(request, 'main/news_category.html', {'news': news, 'categories': categories, 'category': category})
