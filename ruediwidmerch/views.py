from django.shortcuts import render

from .cartoons.models import Cartoon
from .cartoons.models import Category
from .column.models import Column
from .events.models import Event
from .news.models import News
from .portrait.models import Portrait


def home(request):
    cartoons = Cartoon.objects.order_by('ordering')
    categories = Category.objects.all()

    try:
        featured = News.objects.get(featured=True)
    except News.DoesNotExist:
        featured = None

    return render(request, 'index.html', {
        'cartoons': cartoons,
        'categories': categories,
        'featured': featured,
    })


def column(request):
    columns = Column.objects.order_by('-date')
    newest = Column.objects.latest('date')

    return render(request, 'texte.html', {
        'columns': columns,
        'newest': newest,
    })


def single_column(request, id):
    columns = Column.objects.order_by('-date')
    newest = Column.objects.get(id=id)

    return render(request, 'texte.html', {
        'columns': columns,
        'newest': newest,
    })


def news(request):
    newss = News.objects.filter(featured=False)
    events = Event.objects.all()
    try:
        featured = News.objects.get(featured=True)
    except News.DoesNotExist:
        featured = None

    return render(request, 'news.html', {
        'newss': newss,
        'newsall': newss,
        'events': events,
        'featured': featured,
    })


def newsyear(request, year):
    newsall = News.objects.all()
    newss = News.objects.filter(date__year=year)
    events = Event.objects.all()

    return render(request, 'news.html', {
        'currentyear': year,
        'newsall': newsall,
        'newss': newss,
        'events': events,
    })


def portrait(request):
    portraits = Portrait.objects.all()

    return render(request, 'portrait.html', {
        'portraits': portraits,
    })


def contact(request):
    return render(request, 'contact.html', {
    })
