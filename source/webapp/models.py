from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name='Тип задачи')

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.PROTECT,
                               verbose_name='Статус', default='Новый')
    type = models.ManyToManyField('webapp.Type', related_name='tasks', blank=True,
                                  verbose_name='Тип задачи', default='Задача')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.pk} {self.summary}'
