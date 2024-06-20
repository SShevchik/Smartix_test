from django.contrib.auth import models
from django.contrib.auth.hashers import make_password


class UserManager(models.UserManager):
    def get_user_by_pk(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None


class User(models.AbstractUser):
    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
