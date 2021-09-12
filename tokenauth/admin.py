from django.contrib import admin

# Register your models here.

from tokenauth.models import User

admin.site.register(User)
