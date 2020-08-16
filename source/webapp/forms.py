from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Status, Type


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'

# Извините, но более интересные проверки я просто не придумал
def at_least_10(string):
   if len(string) < 10:
       raise ValidationError('Слишком коротко! Минимум 10 символов.')


def at_least_50(string):
    if len(string) < 50:
        raise ValidationError('Слишком коротко! Минимум 50 символов.')


class TaskForm(forms.ModelForm):
    summary = forms.CharField(validators=(at_least_10,), label='Короткое описание')
    description = forms.CharField(validators=(at_least_50,), required=False, widget=forms.Textarea,
                                  label='Подробное описание')

    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']
        widgets = {
            'type': forms.CheckboxSelectMultiple,
        }
