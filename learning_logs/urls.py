"""Определяет схемы URL для learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'  # помогает Django, отличить этот urls.py от других

# список страниц которые могут запрашиваться из приложения learning_logs
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),  # путь(localhost:8000), вьюха, имя
]
