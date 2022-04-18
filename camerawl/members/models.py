from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    """

    """
    # We use the one to one field to extend the standard django user model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The users nickname will be how they are identified on the site.
    # This is specifically so we don't identify the user by any actual name.
    nickname = models.CharField(max_length=100, unique=True)

    # We use this attribute to define if the user is an adult.
    is_adult = models.BooleanField(default=False, verbose_name="is an adult")

    # This is a special flag that will hide any content this user has created.
    # We are calling it the panic switch.
    panic_flag = models.BooleanField(
        default=False, verbose_name="panic switch")

    # Just a fun Avatar field. Based on the ImageField here.
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#imagefield

    avatar = models.ImageField(null=True,
                               upload_to=None,
                               height_field=None,
                               width_field=None,
                               max_length=100)
