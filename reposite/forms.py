# forms_py
from django import forms

from .models import ProjectPrototype, PrototypeMetaElement, ProjectTask
from .schema import PrototypeMetadataForm


class ProjectPrototypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectPrototypeForm, self).__init__(*args, **kwargs)

        basefields = self.Meta.fields
        for i in basefields:
            self.fields[i].label = 'General'
            self.fields[i].label_suffix = self.Meta.label_suffixes[i]

        self.fields['description'].label = 'Description'

        metadata_form = PrototypeMetadataForm()
        for i, j in metadata_form.fields.items():
            self.fields[i] = j

    class Meta:
        model = ProjectPrototype
        fields = ('title', 'creator', 'origin', 'publisher', 'publish_date',  'contributors', 'rights', 'uri', 'active', 'description')
        label_groups = ['General', 'Subject Area', 'Description', 'Language', 'Instructional Context', 'Language Proficiency', 'World Readiness', '21st Century Skills']
        label_suffixes = {
            'title': 'Project Title',
            'creator': 'Author',
            'origin': 'Derived from?',
            'description': 'Description',
            'publisher': 'Publisher',
            'publish_date': 'Publish Date',
            'contributors': 'Contributors',
            'rights': 'Rights',
            'uri': 'URI',
            'active': 'Public/Private'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'creator': forms.HiddenInput(),
            'origin': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'size': '40', 'type': 'date', 'placeholder': 'MM/DD/YYY'}),
            'contributors': forms.TextInput(attrs={'class': 'form-control'}),
            'rights': forms.TextInput(attrs={'class': 'form-control'}),
            'uri': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'active': 'Make public/private',
            'contributors': 'Separate names with a comma'
        }


class ProjectPrototypeCreateForm(ProjectPrototypeForm):
    def __init__(self, *args, **kwargs):
        super(ProjectPrototypeCreateForm, self).__init__(*args, **kwargs)

    def save(self):
        super(ProjectPrototypeCreateForm, self).save()

        for i, j in self.cleaned_data.items():
            if i not in ['title', 'creator', 'origin', 'description', 'publisher', 'publish_date', 'contributors', 'rights', 'uri', 'active'] and j:
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
    def __init__(self, *args, **kwargs):
        super(ProjectPrototypeUpdateForm, self).__init__(*args, **kwargs)
        # Make origin hidden to prevent changing the flip. This will inherently remove the current object,
        # make new one from the specified clone. "Recloning" is equivalent to
        # deleting the current object and cloning a new one from the desired prototype.
        self.fields['origin'].widget = forms.HiddenInput()

    def save(self):
        super(ProjectPrototypeUpdateForm, self).save()

        prev_data = self.instance.data.all()
        for i in prev_data:
            i.delete()

        for i, j in self.cleaned_data.items():
            if i not in ['title', 'creator', 'origin', 'description', 'publisher', 'publish_date', 'contributors', 'rights', 'uri', 'active'] and j:
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

    # class Meta(ProjectPrototypeForm.Meta):




class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = ProjectTask
        fields = ('title', 'prototype_project', 'short_description', 'description', 'sequence_order', 'task_category', 'task_type', 'task_focus', 'task_time', 'technology_tips',
                  'task_extension', 'potential_hurdles')
        labels = {'title': 'Task Title'}
        widgets = {'prototype_project': forms.HiddenInput()}


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = ProjectTask
        fields = ('title', 'prototype_project', 'short_description', 'description', 'sequence_order', 'task_category', 'task_type', 'task_focus', 'task_time', 'technology_tips',
                  'task_extension', 'potential_hurdles')
        labels = {'title': 'Task Title'}



