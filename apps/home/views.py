from lib2to3.fixes.fix_input import context

from django.db.models import Max, Subquery, OuterRef
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from apps.home.forms import CommentForm
from django.core.paginator import Paginator

def home_page(request):
    games = models.Game.objects.prefetch_related('genre').all()[:12]

    most_played = models.Game.objects.order_by('-downloads')[:12]

    best = models.Game.objects.order_by('-downloads').first()

    genres = models.Genre.objects.all()

    max_downloads_per_genre = (
        models.Game.objects
        .values('genre')
        .annotate(max_downloads=Max('downloads'))
    )

    # Игры с максимальными скачиваниями по каждому жанру
    most_downloaded = (
                          models.Game.objects
                          .filter(downloads=Subquery(
                              max_downloads_per_genre.filter(genre=OuterRef('genre')).values('max_downloads')
                          ))
                          .order_by('-downloads', 'genre')
                      )[:10]

    # Самая высокая цена
    price = models.Game.objects.order_by('-downloads').values_list('current_price', flat=True).first()

    context = {
        'games': games,
        'most_played': most_played,
        'best': best,
        'genres': genres,
        'most_downloaded': most_downloaded,
        'price': price,
    }

    return render(request, 'home/index.html', context)


def shop_page(request, genre_name=None, studio_name=None):
    genres = models.Genre.objects.all()
    studios = models.Studio.objects.all()
    games = models.Game.objects.all()
    if genre_name:
        genre = get_object_or_404(models.Genre, slug=genre_name)
        games = games.filter(genre=genre)
    if studio_name:
        studio = get_object_or_404(models.Studio, slug=studio_name)
        games = games.filter(studio=studio)

    paginator = Paginator(games, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'genres': genres,
        'studios': studios,
        'games': page_obj,
    }
    return render(request, 'home/shop.html', context)




def product_detail(request, pk):
    user_wish_item = models.WishLibraryItem.objects.filter(
        library__user=request.user,
        game_id=pk
    ).first()

    game = get_object_or_404(models.Game, pk=pk)
    comments = models.Comment.objects.filter(game=game)
    paginator = Paginator(comments, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    genres = game.genre.all()
    tags = game.tags.all()
    studios = game.studio.all()
    studio = game.studio.first()
    related_games = models.Game.objects.filter(studio__in=studios).exclude(id=game.id)[:5]
    user_cart_item = models.GameLibraryItem.objects.filter(
        library__user=request.user,
        game_id=pk
    ).first()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.game = game
            form.save()
            return redirect('product', pk=game.pk)
    else:
        form = CommentForm()

    context = {
        'game': game,
        'genres': genres,
        'tags': tags,
        'studios': studios,
        'studio': studio,
        'related_games': related_games,
        'comments': page_obj,
        'form': form,
        'user_wish_item': user_wish_item,
        'user_cart_item': user_cart_item,

    }
    return render(request, 'home/product_detail.html', context)



def contact_page(request):
    return render(request, 'home/contact.html')


def cart(request):
    return render(request, 'home/cart.html')


def wish_list(request):
    user = request.user

    items = models.WishLibraryItem.objects.filter(library__user=user)
    context={
        'items':items
    }
    return render(request, 'home/wana_buy.html',context)


def library(request):
    return render(request, 'home/library.html')


def search(request):
    query = request.GET.get('searchKeyword')
    games = []
    if query:
        games = models.Game.objects.filter(name__icontains=query)
    if not games:
        message = "Ничего не найдено."
    else:
        message = ""
    context = {
        'games': games,
        'message': message,
    }
    return render(request, 'home/search.html', context)


def add_to_cart(request, game_id, user_id):
    user = models.User.objects.get(pk=user_id)
    game = models.Game.objects.get(pk=game_id)

    library, created = models.GameLibrary.objects.get_or_create(
        user=user
    )

    item, item_created = models.GameLibraryItem.objects.get_or_create(
        library=library,
        game=game
    )

    return redirect('cart')





def dell_from_cart(request, library_item_id):
    item = models.GameLibraryItem.objects.get(pk=library_item_id)
    item.delete()
    return redirect('cart')


def add_to_wishlibrary(request, game_id, user_id):
    user = models.User.objects.get(pk=user_id)
    game = models.Game.objects.get(pk=game_id)

    library, created = models.WishLibrary.objects.get_or_create(
        user=user
    )

    item, item_created = models.WishLibraryItem.objects.get_or_create(
        library=library,
        game=game
    )

    return redirect('wish')


def wish_add_or_del(request, library_item_id):
    item = models.WishLibraryItem.objects.get(pk=library_item_id)
    item.is_downloaded = not item.is_downloaded

    item.save()
    return redirect('wish_list')


def dell_from_wish(request, library_item_id):
    item = models.WishLibraryItem.objects.get(pk=library_item_id)
    item.delete()
    return redirect('wish')
