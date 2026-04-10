from django.shortcuts import render, redirect

def get_popular_tags():
    return ['python', 'django', 'mysql', 'perl', 'javascript']

def get_best_members():
    return ['Поздышев Александр', 'Опритов Артём', 'Виндман Александр']


def login(request):
    context = {
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'core/login.html', context)


def logout(request):
    return redirect('index')


def signup(request):
    context = {
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'core/signup.html', context)


def profile(request):
    context = {
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'core/profile.html', context)


def ask(request):
    context = {
        'popular_tags': get_popular_tags(),
        'best_members': get_best_members(),
    }
    return render(request, 'core/ask.html', context)
