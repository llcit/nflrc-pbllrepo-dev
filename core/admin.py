from django.contrib import admin

from reposite.models import ProjectPrototype, PrototypeMetaElement, ProjectTask, ProjectFile, ProjectComment
from discussions.models import Post


class ProjectPrototypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'origin', 'active')
    list_filter = ['creator', 'origin', 'active']
    list_editable = ['active']


class PrototypeMetaElementAdmin(admin.ModelAdmin):
    list_display = ('prototype_project', 'element_type', 'element_data')
    list_filter = ['prototype_project', 'element_type', 'element_data']


class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ('prototype_project', 'creator',
                    'task_category', 'title', 'sequence_order')
    list_filter = ['prototype_project']
    list_editable = ['task_category', 'title', 'sequence_order']


class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_file', 'project')

admin.site.register(ProjectPrototype, ProjectPrototypeAdmin)
admin.site.register(PrototypeMetaElement, PrototypeMetaElementAdmin)
admin.site.register(ProjectTask, ProjectTaskAdmin)
admin.site.register(ProjectFile, ProjectFileAdmin)
admin.site.register(ProjectComment)

admin.site.register(Post)
