from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = 'jobs'
        app_label = 'jobs'
