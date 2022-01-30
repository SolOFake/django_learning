from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # обращение к классу модели
        fields = ['text']  # обращение к имени поля модели
        labels = {'text': ''}  # не генерировать подпись для текстового поля. label в html


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
