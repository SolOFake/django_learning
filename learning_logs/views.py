from django.shortcuts import render

from .models import Topic


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
