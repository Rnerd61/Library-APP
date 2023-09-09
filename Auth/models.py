from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class UserModel(AbstractBaseUser):
    username = None
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def has_perm(self, perm, obj=None):
        return self.is_staff
    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email

