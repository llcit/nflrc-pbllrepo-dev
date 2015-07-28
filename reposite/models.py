import string
import random
from collections import OrderedDict, namedtuple

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from filebrowser.fields import FileBrowseField

from discussions.models import Post

from .schema import PrototypeMetadataForm


class ProjectPrototype(TimeStampedModel):
    title = models.CharField(max_length=512, unique=True)
    creator = models.ForeignKey(User, related_name='projects')
    origin = models.ForeignKey(
        'self', null=True, blank=True, related_name='flips')
    description = models.TextField(default='Describe your project here.')
    publisher = models.CharField(
        max_length=512, default='National Foreign Language Resource Center')
    publish_date = models.DateField(null=True, blank=True)
    contributors = models.TextField(null=True, blank=True)
    rights = models.CharField(max_length=512, null=True, blank=True)
    uri = models.CharField(max_length=512, null=True, blank=True)
    active = models.BooleanField(
        default=False, help_text="Hide/unhide this project")
    icon = models.FileField(
        upload_to='uploads', null=True, blank=True)

    def clone_project(self, user):
        rstr = ''.join(
            random.choice(string.ascii_lowercase + string.digits) for x in range(4))
        new_title = self.title + '-' + user.last_name + '-' + rstr

        try:
            # Copy object attributes
            clone = ProjectPrototype(
                title=new_title, creator=user, origin=self, description=self.description, publisher=self.publisher, rights=self.rights)
            clone.save()

            # Copy object metadata
            for i in self.data.all():
                pm = PrototypeMetaElement(
                    prototype_project=clone, element_type=i.element_type, element_data=i.element_data)
                pm.save()

            # Copy object tasks
            for i in self.tasks.all():
                new_t = i.clone_task()
                new_t.prototype_project = clone
                new_t.save()

        except:
            pass

        return clone

    def meta_data_schema(self):
        return PrototypeMetadataForm()

    def get_element_data(self, element_type):
        data = [i.element_data for i in self.data.filter(
            element_type=element_type)]
        return data

    def get_data_dict(self):
        """ Group element data by element_type. Returns a dict keyed by element_type name. """

        """
        Using a namedtuple here to gather display string and data items.
        """
        MetaElement = namedtuple(
            'MetaElement', 'metaprefix displayname datalist')
        data_dict = OrderedDict()
        field_order = self.meta_data_schema().fields.items()

        for field_name, field_type in field_order:
            data_dict[field_name] = MetaElement(
                metaprefix=field_type.label,
                displayname=field_type.label_suffix,
                datalist=[]
            )

        for i in self.data.all().order_by('element_type'):
            try:
                data_dict[i.element_type].datalist.append(i.element_data)
            except:
                data_dict[i.element_type] = []
                data_dict[i.element_type].append(i.element_data)

        return data_dict

    def save(self, *args, **kwargs):
        """ Create comment thread if one does not exist"""


        super(ProjectPrototype, self).save(*args, **kwargs)
        if not ProjectComment.objects.filter(project=self):
            thread = Post(text='Project Comments', creator=self.creator, subject='Comments for project')
            thread.save()
            ProjectComment(thread=thread, project=self).save()

    def get_absolute_url(self):
        return reverse('view_prototype', args=[self.id])

    def __unicode__(self):
        return self.title


class PrototypeMetaElement(models.Model):
    prototype_project = models.ForeignKey(
        ProjectPrototype, related_name='data')
    element_type = models.CharField(max_length=512)
    element_data = models.TextField()

    class Meta:
        unique_together = (
            ('prototype_project', 'element_type', 'element_data'),)


TASK_CATEGORIES = (
    ('0_preparing', 'Preparing'),
    ('1_launching', 'Launching'),
    ('2_managing', 'Managing'),
    ('3_assessment', 'Assessment')
)

TASK_TYPES = (
    ('driving question', 'Driving question'),
    ('need to know', 'Need to know'),
    ('scaffolding', 'Scaffolding')
)

TASK_FOCI = (
    ('content', 'Content'),
    ('grammar', 'Grammar'),
    ('interaction', 'Interaction'),
    ('technology', 'Technology')
)


class ProjectTask(models.Model):
    title = models.CharField(max_length=512)
    short_description = models.TextField(
        default='A sentence that summarizes this task.')
    task_category = models.CharField(
        max_length=48, blank=True, null=True, choices=TASK_CATEGORIES)
    task_type = models.CharField(max_length=48, blank=True, choices=TASK_TYPES)
    task_focus = models.CharField(max_length=48, blank=True, choices=TASK_FOCI)
    task_time = models.CharField(max_length=48, blank=True)
    description = models.TextField()
    technology_tips = models.TextField(blank=True)
    task_extension = models.TextField(blank=True)
    potential_hurdles = models.TextField(blank=True)
    prototype_project = models.ForeignKey(
        ProjectPrototype, null=False, related_name='tasks')
    sequence_order = models.IntegerField(default=0)

    def creator(self):
        return self.prototype_project.creator

    def clone_task(self):
        t1 = self
        t1.pk = None
        t1.save()
        return t1

    def get_absolute_url(self):
        return reverse('view_task', args=[self.prototype_project.id, self.id])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['task_category', 'sequence_order']


class ProjectFile(TimeStampedModel):
    project_file = models.FileField(
        upload_to='uploads', null=True, blank=True)
    project = models.ForeignKey(ProjectPrototype, null=True, blank=True, related_name='project_files')
    user = models.ForeignKey(User, related_name='uploaded_files')


class ProjectComment(models.Model):
    thread = models.ForeignKey(Post, related_name='project_thread')
    project = models.ForeignKey(ProjectPrototype, related_name='project_discussion')

    class Meta:
        verbose_name = 'Project / Discussion Pair'

    def __unicode__(self):
        return '%s --> %s' % (self.project, self.thread)
