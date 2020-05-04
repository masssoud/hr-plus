from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    team = models.ForeignKey('Team', blank=True, null=True, on_delete=models.SET_NULL)
    can_view_teams = models.ManyToManyField('Team', related_name='profile_can_view_teams')
    can_view_projects = models.ManyToManyField('Project', related_name='profile_can_view_projects')
    works_on_projects = models.ManyToManyField('Project', related_name='profile_works_on_projects')

    class Meta:
        db_table = 'profiles'
        app_label = 'users'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        full_name = '{} {}'.format(self.user.first_name, self.user.last_name)
        if full_name.strip() == '':
            full_name = self.user.username
        return full_name.strip()
