from django.db import models


class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    is_open = models.BooleanField(default=True, db_index=True)
    description = models.TextField(default="", blank=True)
    qualifications = models.TextField(default="", blank=True)
    requirements = models.TextField(default="", blank=True)
    good_to_have = models.TextField(default="", blank=True)
    benefits = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_postings'
        app_label = 'jobs'

    def __str__(self):
        return self.title