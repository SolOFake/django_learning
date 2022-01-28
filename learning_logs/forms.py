from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # обращение к классу модели
        fields = ['text']  # обращение к имени поля модели
        labels = {'text': ''}  # не генерировать подпись для текстового поля. label в html
