from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)

    def __unicode__(self):
        return "{} - {} - Out: {}".format(self.title,
                                          self.location,
                                          self.employer)
