from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

