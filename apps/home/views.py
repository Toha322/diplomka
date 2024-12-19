from django.db.models import Count
from django.shortcuts import render
from . import models
from django.db.models import Count
def home_page(request):
    games = models.Game.objects.all()
    most_played=models.Game.objects.all().order_by('-downloads')
    best=models.Game.objects.all().order_by('-downloads').first
    genres = models.Genre.objects.all()
    most_downloaded = (models.Game.objects
                       .values('genre')  # Группировка по жанру
                       .annotate(num_games=Count('id'))  # Подсчёт количества игр в каждом жанре
                       .order_by('-num_games', 'genre'))




    context = {
        'games': games,
        'most_played': most_played,
        'best':best,
        'genres':genres,
        'most_downloaded':most_downloaded

    }
    return render(request, 'home/index.html', context)

def shop_page(request):
    return render(request,'home/shop.html')

def product_detail(request):
    return render(request,'home/product_detail.html')

def contact_page(request):
    return render(request,'home/contact.html')
