from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Task, Type, Status
from django.views.generic import View, TemplateView, FormView
from .forms import TaskForm, BROWSER_DATETIME_FORMAT


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return render(request, 'view.html', context)


class CreateView(FormView):
    template_name = 'create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')


class UpdateView(FormView):
    template_name = 'update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    # def get_initial(self):
    #     return {'publish_at': make_naive(self.article.publish_at)\
    #         .strftime(BROWSER_DATETIME_FORMAT)}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)
