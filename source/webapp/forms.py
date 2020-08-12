from django import forms
from .models import Status, Type


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Краткое описание')
    description = forms.CharField(required=False, label='Полное описание', widget=forms.Textarea)
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип задачи',
                                          widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), initial='Новый', label='Статус')
