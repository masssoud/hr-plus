from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'categories'
        app_label = 'jobs'
