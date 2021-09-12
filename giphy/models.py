from django.db import models
from tokenauth.models import User
from tags.models import Tags

# Create your models here.

class Giph(models.Model):
    url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.url
