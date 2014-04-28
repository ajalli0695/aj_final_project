from django.views import generic
from .models import Job


class ListJobsView(generic.TemplateView):
    template_name = 'listjobs/jobs.html'
