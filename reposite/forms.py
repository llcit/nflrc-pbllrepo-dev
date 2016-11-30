# forms_py
from django import forms
from django.forms import ClearableFileInput

# from filebrowser.widgets import ClearableFileInput

from .models import ProjectPrototype, PrototypeMetaElement, ProjectTask, ProjectFile
from .schema import PrototypeMetadataForm


class ProjectPrototypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectPrototypeForm, self).__init__(*args, **kwargs)

        """ Set up the local fields first """
        basefields = self.Meta.fields
        for i in basefields:
            self.fields[i].label = 'General'
            self.fields[i].label_suffix = self.Meta.label_suffixes[i]

        """ Give the description field its own group. Other fields can also be adjusted here if needed. """
        self.fields['description'].label = 'Description'

        """ Now set up the schema fields  """
        metadata_form = PrototypeMetadataForm()
        for i, j in metadata_form.fields.items():
            self.fields[i] = j

    class Meta:
        model = ProjectPrototype

        """ Base model fields (i.e., these descriptors are NOT specified in schema but with the model) """
        fields = ('title', 'icon', 'creator', 'origin', 'publisher', 'publish_date',  'contributors', 'rights', 'uri', 'active', 'description')

        """ Label groups identify related groups. These are assigned in init or in PrototypeMetadataForm """
        label_groups = ['General', 'Subject Area', 'Description', 'Language', 'Instructional Context', 'Language Proficiency', 'World Readiness Standards', '21st Century Skills']

        """ Label  suffixes are used to label each item within a label group """
        label_suffixes = {
            'title': 'Project Title',
            'icon': 'Project Icon',
            'creator': 'Author',
            'origin': 'Derived from?',
            'description': 'Description',
            'publisher': 'Publisher',
            'publish_date': 'Publish Date',
            'contributors': 'Contributors',
            'rights': 'Rights',
            'uri': 'URI',
            'active': 'Public'
        }

        """
        Note: Making origin field hidden to prevent changing/creating a flip.
        Doing so will inherently reclone: remove the current object and
        make a new one from the specified clone. "Recloning" is equivalent to
        deleting the current object and cloning a new one from the desired prototype.
        We won't handle that complexity here for the sake of clarity.
        """

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': ClearableFileInput(attrs={'class': 'form-control'}),
            'creator': forms.HiddenInput(),
            'origin': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'size': '40', 'type': 'date', 'placeholder': 'MM/DD/YYY'}),
            'contributors': forms.TextInput(attrs={'class': 'form-control'}),
            'rights': forms.TextInput(attrs={'class': 'form-control'}),
            'uri': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'active': 'Display on Web',
            'contributors': 'Separate names with a comma'
        }


class ProjectPrototypeCreateForm(ProjectPrototypeForm):

    def save(self):
        super(ProjectPrototypeCreateForm, self).save()

        """ Create metadata objects from form data skipping fields listed in self.Meta.fields (base fields) """
        for i, j in self.cleaned_data.items():
            if i not in self.Meta.fields and j:
                if type(j) == list:
                    for k in j:
                        pm = PrototypeMetaElement(
                            prototype_project=self.instance, element_type=i, element_data=k)
                        pm.save()
                else:
                    pm = PrototypeMetaElement(
                        prototype_project=self.instance, element_type=i, element_data=j)
                    pm.save()
        return self.instance


class ProjectPrototypeUpdateForm(ProjectPrototypeForm):

    def save(self):
        super(ProjectPrototypeUpdateForm, self).save()

        prev_metadata = self.instance.data.all()

        """ Clear all previously assigned metadata objects """
        for i in prev_metadata:
            i.delete()

        """ Reassign metadata objects from form data skipping fields listed in self.Meta.fields (base fields) """
        for i, j in self.cleaned_data.items():

            if i not in self.Meta.fields and j:
                if type(j) == list:
                    for k in j:
                        pm = PrototypeMetaElement(
                            prototype_project=self.instance, element_type=i, element_data=k)
                        pm.save()
                else:
                    pm = PrototypeMetaElement(
                        prototype_project=self.instance, element_type=i, element_data=j)
                    pm.save()

        return self.instance


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = ProjectTask
        fields = ('title', 'prototype_project', 'short_description', 'description', 'sequence_order', 'task_category', 'task_type', 'task_focus', 'task_time', 'technology_tips',
                  'task_extension', 'potential_hurdles')
        labels = {'title': 'Task Title'}
        widgets = {
            'prototype_project': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'technology_tips': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'task_extension': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'potential_hurdles': forms.Textarea(attrs={'class': 'form-control content-editor'})
        }


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = ProjectTask
        fields = ('title', 'prototype_project', 'short_description', 'description', 'sequence_order', 'task_category', 'task_type', 'task_focus', 'task_time', 'technology_tips',
                  'task_extension', 'potential_hurdles')
        labels = {'title': 'Task Title'}
        widgets = {
            'prototype_project': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'technology_tips': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'task_extension': forms.Textarea(attrs={'class': 'form-control content-editor'}),
            'potential_hurdles': forms.Textarea(attrs={'class': 'form-control content-editor'})
        }


class FileUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(FileUploadForm, self).__init__(*args, **kwargs)
        # self.Meta.fields['project'].choices = self.request.user.projects.all()

    class Meta:
        model = ProjectFile
        fields = ('project_file', 'project', 'user')
        widgets = {'user': forms.HiddenInput(), 'project_file': ClearableFileInput()}



