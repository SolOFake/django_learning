from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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


def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Вывести пустую или недействительную форму.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':  # GET
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)  # форма заранее заполненная информацией из существующего объекта,
    else:                                 # видно существующие записи и можно отредактировать их
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)  # обработка
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
