from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User




class UserManager(BaseUserManager):

    def create_user(self, email, password, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('Username must be set')

        self.model = User
        user = self.model(email=email, **extra_fields)

        if is_superuser:
            user.is_superuser = True

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        is_superuser = True
        return self.create_user(email, password, is_superuser, **extra_fields)


class User(AbstractBaseUser,):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label = 'api'
        db_table = "api_user"

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.email