# mixins.py


class ListUserFilesMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ListUserFilesMixin, self).get_context_data(**kwargs)
        if self.request.user:
            context['filelisting'] = self.request.user.uploaded_files.all()
        return context
