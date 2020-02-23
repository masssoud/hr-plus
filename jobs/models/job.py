from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    good_to_have = models.TextField()
    is_open = models.BooleanField(default=True, db_index=True)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'jobs'
        app_label = 'jobs'
