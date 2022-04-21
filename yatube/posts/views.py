from django.shortcuts import render, get_object_or_404

from .models import Group, Post

POSTS_SHOW = 10


def index(request):
    # в переменную posts будет сохранена выборка из 10 объектов
    # модели Post, отсортированных по полю pub_date
    # по убыванию (от больших значений к меньшим)
    posts = Post.objects.all()[:POSTS_SHOW]
    context = {
        'posts': posts,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_SHOW]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
