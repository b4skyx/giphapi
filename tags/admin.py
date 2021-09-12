from django.contrib import admin

# Register your models here.

from tags.models import Tags

admin.site.register(Tags)
