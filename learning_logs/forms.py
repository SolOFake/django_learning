from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        # приказывает Django не генерировать подпись для текстового поля
        labels = {'text': ''}
