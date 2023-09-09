from django.db import models


class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=64, null=False, blank=False)
    role = models.CharField(max_length=20, choices=[('User','User'),('Admin','Admin')], default="User")

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
