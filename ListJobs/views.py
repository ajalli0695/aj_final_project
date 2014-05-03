from django.views import generic
from .models import Job


class ListJobsView(generic.ListView):
    model = Job
    template_name = 'listjobs/jobs.html'
