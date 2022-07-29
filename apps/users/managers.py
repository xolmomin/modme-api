from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Manager


class ActiveUserManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('User must have a phone number!')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        user = self.create_user(phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
