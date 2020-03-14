from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):
    applicant = models.ForeignKey('Applicant', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), default=None, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'applicant_comments'
        app_label = 'jobs'
        ordering = ['created_at']

    def __str__(self):
        return 'Comment for {} by {}'.format(self.applicant.full_name, self.user.username)
