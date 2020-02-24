from django.contrib import admin

from .models import JobPosting
from .models import Category
from .models import Applicant

admin.site.register(JobPosting)
admin.site.register(Category)
admin.site.register(Applicant)
