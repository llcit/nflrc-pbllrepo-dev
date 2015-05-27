
from collections import OrderedDict

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from braces.views import LoginRequiredMixin

from .models import ProjectPrototype, ProjectTask
from .forms import ProjectPrototypeCreateForm, ProjectPrototypeUpdateForm, TaskCreateForm, TaskUpdateForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['prototype_list'] = ProjectPrototype.objects.all()
        return context


class ProjectPrototypeDocumentView(DetailView):
    model = ProjectPrototype
    template_name = 'project_prototype_doc.html'
    context_object_name = 'project_prototype'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeDocumentView, self).get_context_data(**kwargs)
        project = self.get_object()

        """ tasks are keyed by task_category """
        tasks = OrderedDict()
        for i in project.tasks.all():
            try:
                tasks[i.get_task_category_display()].append(i)
            except:
                tasks[i.get_task_category_display()] = []
                tasks[i.get_task_category_display()].append(i)

        context['tasks'] = tasks
        context['description'] = project.description

        return context


class CloneProjectView(LoginRequiredMixin, DetailView):
    model = ProjectPrototype
    template_name = 'project_prototype_detail.html'
    context_object_name = 'project_prototype'

    def dispatch(self, request, *args, **kwargs):
        clone = self.get_object().clone_project(self.request.user)
        if clone:
            return HttpResponseRedirect(reverse('update_prototype', args=[clone.id]))

        return super(CloneProjectView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CloneProjectView, self).get_context_data(**kwargs)
        context['prototype_data'] = self.get_object().get_data_dict()
        return context


class ProjectPrototypeListView(TemplateView):
    template_name = 'project_prototype_list.html'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeListView, self).get_context_data(**kwargs)
        prototypes = []
        for i in ProjectPrototype.objects.all().order_by('-active'):
            proto = (i, i.get_data_dict())
            prototypes.append(proto)

        context['prototype_list'] = prototypes
        return context


class ProjectPrototypeDetailView(DetailView):
    model = ProjectPrototype
    template_name = 'project_prototype_detail.html'
    context_object_name = 'project_prototype'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeDetailView, self).get_context_data(**kwargs)
        context['prototype_data'] = self.get_object().get_data_dict()
        context['prototype_tasks'] = self.get_object().tasks.all()
        return context


class ProjectPrototypeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProjectPrototype
    template_name = 'project_prototype_create_update.html'
    context_object_name = 'project_prototype'
    form_class = ProjectPrototypeCreateForm
    success_message = "Your new project looks great! Perhaps you can put your mind to the tasks :)!"


    def get_initial(self):
        """ Returns the initial data to use for forms on this view. """
        initial = self.initial.copy()
        initial['creator'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeCreateView, self).get_context_data(**kwargs)
        context['edit_text'] = 'Adding New Project'
        return context


class ProjectPrototypeUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectPrototype
    template_name = 'project_prototype_create_update.html'
    context_object_name = 'project_prototype'
    form_class = ProjectPrototypeUpdateForm

    def get_initial(self):
        """ Returns the initial metadata to use for forms on this view. """
        choice_fields = self.get_object().meta_data_schema().multiple_choice_fields()

        initial = self.initial.copy()
        for i in self.get_object().data.all():
            if i.element_type in choice_fields:
                try:
                    initial[i.element_type].append(i.element_data)
                except:
                    initial[i.element_type] = [i.element_data]
            else:
                initial[i.element_type] = i.element_data

        return initial

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeUpdateView, self).get_context_data(**kwargs)

        context['edit_text'] = 'Updating'
        return context


class ProjectPrototypeDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectPrototype
    template_name = 'project_prototype_delete_confirm.html'
    context_object_name = 'project_prototype'
    success_url = reverse_lazy('home')


class ProjectTaskListView(DetailView):
    model = ProjectPrototype
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskListView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.get_object()
        context['task_list'] = self.get_object().tasks.all()
        if context['task_list']:
            context['project_task'] = context['task_list'][0]
        return context


class ProjectTaskDetailView(DetailView):
    model = ProjectTask
    template_name = 'task_detail.html'
    context_object_name = 'project_task'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskDetailView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.get_object().prototype_project
        context['task_list'] = context['prototype_project'].tasks.all()
        return context


class ProjectTaskCreateView(LoginRequiredMixin, CreateView):
    model = ProjectTask
    template_name = 'task_create_update.html'
    context_object_name = 'project_task'
    form_class = TaskCreateForm
    project = None

    def get_initial(self):
        initial = self.initial.copy()
        try:
            self.project = ProjectPrototype.objects.get(
                pk=self.kwargs['project'])
            initial['prototype_project'] = self.project.id
        except:
            pass

        return initial

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskCreateView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.project

        return context


class ProjectTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectTask
    template_name = 'task_create_update.html'
    context_object_name = 'project_task'
    form_class = TaskUpdateForm


class ProjectTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectTask
    template_name = 'task_delete_confirm.html'
    context_object_name = 'project_task'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('view_prototype', args=[self.get_object().prototype_project.id, ])
