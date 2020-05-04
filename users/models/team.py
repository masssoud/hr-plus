from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    parent_team = models.ForeignKey('Team', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'
        app_label = 'users'

    def __str__(self):
        return self.name
