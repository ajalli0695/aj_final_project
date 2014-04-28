from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import ListJobsView


class ListJobs(TestCase):
    def test_list_jobs_url(self):
        jobs = resolve(reverse('listjobs:jobs'))
        return self.assertEqual(jobs.func.__name__,
                                ListJobsView.__name__)
