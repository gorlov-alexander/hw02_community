from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
posts_show = 10


def index(request):

    # в переменную posts будет сохранена выборка из 10 объектов
    # модели Post, отсортированных по полю pub_date
    # по убыванию (от больших значений к меньшим)
    posts = Post.objects.all()[:posts_show]
    template = 'posts/index.html'
    context = {
        'posts': posts,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).all()[:posts_show]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
