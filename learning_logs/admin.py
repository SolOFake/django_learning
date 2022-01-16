from django.contrib import admin

from .models import Topic, Entry

# регистрация таблиц моделей в админке
admin.site.register(Topic)
admin.site.register(Entry)
