from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from news.models import News

def news_view(request):
    news_show = News.objects.filter(status=True).order_by('-register_time')
    news_important = News.objects.filter(status=1,importance=1).order_by('-register_time')[:5]
    for news in news_important:
        news.body = news.body[:100]
    for news in news_show:
        news.body = news.body[:400]
    context = {'news' : news , 'news_show' : news_show,}
    return render(request,'news/index.html', context=context)

def news_details(request,news_id):
    news = get_object_or_404(News, id=news_id)
    news_important = News.objects.filter(status=1,importance=1).order_by('-register_time')[:5]
    for new in news_important:
        new.body = new.body[:100]
    context = { 'news' : news ,'news_important': news_important, }
    return render(request, 'news/news.html', context=context)