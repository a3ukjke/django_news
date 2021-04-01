from django.shortcuts import render
from .models import News, Category
from django.http import HttpResponse

def index(request):
    #print(request)
    #news = News.objects.all()
    #res = '<h1>Список новостей</h1>'
    #for item in news:
    #    res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    #return HttpResponse(res)

    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news':news, 
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)



# def test(request):
#     return HttpResponse('<h1>Тестовая страница</h1>')

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})
