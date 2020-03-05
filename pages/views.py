from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from general.models import Rules
from product.models import Product
from news.models import News

def index(request):
    news_important = News.objects.filter(status=1,importance=1).order_by('-register_time')[:5]
    for news in news_important:
        news.body = news.body[:100] 
    products_recent = Product.objects.filter(status=1).order_by('-register_time')[:8]
    context = { 'products_recent' : products_recent ,'news_important' :news_important ,}
    return render(request, 'pages/index.html', context=context)



def rules(request):
    rules = get_object_or_404(Rules, id=1)
    context = { 'rules' : rules ,}
    return render(request, 'pages/rules.html', context=context)
