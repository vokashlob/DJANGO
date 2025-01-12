from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.
def sign_up_by_html(request):
    info = {'title': 'Регистрация пользователя с помощью HTML-формы'}
    users = ['user', 'admin']
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        age = request.POST.get('age')

        if login not in users and password == password_repeat and int(age) >= 18:
            return HttpResponse(f'Приветствуем, {login}')
        else:
            if login in users:
                info['error'] = 'Пользователь уже существует'
            elif password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    info = {'title': 'Регистрация пользователя с помощью Django-формы'}
    users = ['user', 'admin']
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            age = form.cleaned_data['age']

            if login not in users and password == password_repeat and int(age) >= 18:
                return HttpResponse(f'Приветствуем, {login}')
            else:
                if login in users:
                    info['error'] = 'Пользователь уже существует'
                elif password != password_repeat:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) < 18:
                    info['error'] = 'Вы должны быть старше 18 лет'
    else:
        info['form'] = RegisterForm()
    return render(request, 'fifth_task/registration_page.html', context=info)