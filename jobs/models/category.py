from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'categories'
        app_label = 'jobs'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
