from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # Позволяет изменять поле group в любом посте прямо из списка постов
    list_editable = ('group',)
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
