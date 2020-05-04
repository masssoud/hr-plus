from django.db import models
from softdelete.models import SoftDeleteModel


class Project(SoftDeleteModel):
    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'
        app_label = 'users'

    def __str__(self):
        return self.name
