
from collections import OrderedDict
import HTMLParser


from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from braces.views import LoginRequiredMixin
from haystack.generic_views import SearchView

from core.mixins import ListUserFilesMixin
from discussions.forms import PostReplyForm

from .models import ProjectPrototype, ProjectTask, ProjectFile, ProjectComment
from .forms import ProjectPrototypeCreateForm, ProjectPrototypeUpdateForm, TaskCreateForm, TaskUpdateForm, FileUploadForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #context['prototype_list'] = ProjectPrototype.objects.all() <-- modified 6/23/2016 to filter by active (display on web only public ones)
        prototypes = ProjectPrototype.objects.all().filter(active=True)
        context['prototype_list'] = prototypes

        languages = {}
        for i in prototypes:
            for j in i.get_languages():
                try:
                    languages[j] = languages[j] + 1
                except:
                    languages[j] = 1

        context['languages'] = languages

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

        thread = ProjectComment.objects.get(project=project).thread or None
        initial_post_data = {}
        initial_post_data['creator'] = self.request.user
        initial_post_data['subject'] = 'Re: %s' % project.title
        initial_post_data['parent_post'] = thread
        form = PostReplyForm(initial=initial_post_data)

        context['tasks'] = tasks
        context['description'] = project.description
        context['thread'] = ProjectComment.objects.get(project=project).thread
        context['comments'] = thread.replies.filter(deleted=False)
        context['postform'] = form
        try:
            context['filelisting'] = project.project_files.all()
        except:
            context['filelisting'] = None
        return context


class CloneProjectView(LoginRequiredMixin, DetailView):
    model = ProjectPrototype
    template_name = 'project_prototype_detail.html'
    context_object_name = 'project_prototype'

    def get(self, request, *args, **kwargs):
        clone = self.get_object().clone_project(self.request.user)
        if clone:
            objstr = self.get_object().title
            messages.add_message(request, messages.INFO, 'You have just flipped ' + objstr + '! You might want to rename it to give it your special stamp.')
            return HttpResponseRedirect(reverse('update_prototype', args=[clone.id]))

        return super(CloneProjectView, self).get(request, *args, **kwargs)

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
        #for i in ProjectPrototype.objects.all().order_by('-active'): <-- modified 6/23/2016 filter by active (display on web only public ones)
        for i in ProjectPrototype.objects.all().filter(active=True):
            proto = (i, i.get_data_dict())
            prototypes.append(proto)
        
        languages = {}
        for i in prototypes:
            for j in i[0].get_languages():
                try:
                    languages[j] = languages[j] + 1
                except:
                    languages[j] = 1

        context['languages'] = languages
        context['prototype_list'] = prototypes
        return context


class ProjectPrototypeDetailView(DetailView):
    model = ProjectPrototype
    template_name = 'project_prototype_detail.html'
    context_object_name = 'project_prototype'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectPrototypeDetailView, self).get_context_data(**kwargs)
        
        context['prototype_data'] = self.get_object().get_data()
        
        tasks = OrderedDict()
        for i in self.get_object().tasks.all():
            try:
                tasks[i.get_task_category_display()].append(i)
            except:
                tasks[i.get_task_category_display()] = []
                tasks[i.get_task_category_display()].append(i)

        context['user_is_coeditor'] = self.get_object().coeditors.filter(coeditor=self.request.user)
        if not context['user_is_coeditor']:
            context['user_is_coeditor'] = self.request.user.is_staff

        context['prototype_tasks'] = tasks  # self.get_object().tasks.all()
        context['task_list'] = self.get_object().tasks.all()
        return context


class ProjectPrototypeCreateView(LoginRequiredMixin, SuccessMessageMixin, ListUserFilesMixin, CreateView):
    model = ProjectPrototype
    template_name = 'project_prototype_create_update.html'
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
        return context


class ProjectPrototypeUpdateView(LoginRequiredMixin, ListUserFilesMixin, UpdateView):
    model = ProjectPrototype
    template_name = 'project_prototype_create_update.html'
    context_object_name = 'project_prototype'
    form_class = ProjectPrototypeUpdateForm

    def get_initial(self):
        """ Returns the initial metadata to use for forms on this view. """
        choice_fields = self.get_object().meta_data_schema().multiple_choice_fields()

        initial = self.initial.copy()

        """ Initialize from metadata values """
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
        # context['tasks'] = self.get_object().tasks.all()
        # context['edit_text'] = 'Edit'
        return context


class ProjectPrototypeDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectPrototype
    template_name = 'project_prototype_delete_confirm.html'
    context_object_name = 'project_prototype'
    success_url = reverse_lazy('list_prototypes')


class ProjectTaskListView(LoginRequiredMixin, DetailView):
    model = ProjectPrototype
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskListView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.get_object()
        context['task_list'] = self.get_object().tasks.all()
        if context['task_list']:
            context['project_task'] = context['task_list'][0]
        context['user_is_coeditor'] = context['prototype_project'].coeditors.filter(coeditor=self.request.user)
        if not context['user_is_coeditor']:
            context['user_is_coeditor'] = self.request.user.is_staff        
        return context


class ProjectTaskDetailView(LoginRequiredMixin, ListUserFilesMixin, DetailView):
    model = ProjectTask
    template_name = 'task_detail.html'
    context_object_name = 'project_task'

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskDetailView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.get_object().prototype_project
        context['task_list'] = context['prototype_project'].tasks.all()
        context['user_is_coeditor'] = context['prototype_project'].coeditors.filter(coeditor=self.request.user)
        if not context['user_is_coeditor']:
            context['user_is_coeditor'] = self.request.user.is_staff

        return context


class ProjectTaskCreateView(LoginRequiredMixin, ListUserFilesMixin, CreateView):
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
        context['edit_text'] = 'Adding a new task to'
        return context


class ProjectTaskUpdateView(LoginRequiredMixin, ListUserFilesMixin, UpdateView):
    model = ProjectTask
    template_name = 'task_create_update.html'
    context_object_name = 'project_task'
    form_class = TaskUpdateForm

    def get_context_data(self, **kwargs):
        context = super(
            ProjectTaskUpdateView, self).get_context_data(**kwargs)
        context['prototype_project'] = self.get_object().prototype_project
        context['edit_text'] = 'Updating a task for'
        return context


class ProjectTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectTask
    template_name = 'task_delete_confirm.html'
    context_object_name = 'project_task'

    def get_success_url(self):
        return reverse('view_prototype', args=[self.get_object().prototype_project.id, ])


class FileUploadView(LoginRequiredMixin, ListUserFilesMixin, CreateView):
    model = ProjectFile
    template_name = 'file_upload.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('upload_file')

    def get_initial(self):
        project = self.request.GET.get('p', None)
        initial = self.initial.copy()
        try:
            initial['user'] = self.request.user
            if project:
                initial['project'] = ProjectPrototype.objects.get(pk=project)
        except:
            pass
        return initial


class ProjectFileDeleteView(LoginRequiredMixin, ListUserFilesMixin, DeleteView):
    model = ProjectFile
    template_name = 'project_file_delete_confirm.html'
    success_url = reverse_lazy('upload_file')


class SearchHaystackView(SearchView):
    def get_queryset(self):
        queryset = super(SearchHaystackView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SearchHaystackView, self).get_context_data(*args, **kwargs)
        
        return context

