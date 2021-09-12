from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            return TypeError("Email is required.")
        if not password:
            return TypeError("Password is required.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        user.save()

        return user

    def create_superuser(self, email, password):
        if not email:
            return TypeError("Email is required.")
        if not password:
            return TypeError("Password is required.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager() #pyright: reportGeneralTypeIssues=none

    def __str__(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
