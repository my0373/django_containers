from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    """

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    is_parent = models.BooleanField(default=False)
