from django.shortcuts import render
# from django.views.generic import TemplateView
# Create your views here.


def  platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'third_task/platform.html', context)


def games(request):
    title = 'Игры'
    games = ['Poker Superstars', 'The Talos Principle', 'Uncrashed', 'Liftoff', 'Portal Revolution']
    back_url = "../platform"
    context = {
        'title': title,
        'games': games,
        'back_url': back_url
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    title = 'Корзина'
    back_url = "../platform"
    context = {
        'title': title,
        'back_url': back_url
    }
    return render(request, 'third_task/cart.html', context)
