from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Выводит список тем."""

    # Выдается запрос к базе данных на получение объектов Topic,
    # отсортированных по атрибуту date_added
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}  # передается шаблону
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    # Между topic.id и topic_id существует неочевидное,
    # но важное различие. Выражение topic.id проверяет тему и получает
    # значение соответствующего идентификатора. Переменная topic_id содержит
    # ссылку на этот идентификатор в коде. Если вы столкнетесь с ошибками при
    # работе с идентификаторами, убедитесь в том, что эти выражения
    # используются правильно.


def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)  # принимает данные пользователя введенные в форму request.POST
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')  # редирект после добавления темы, к списку тем
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
