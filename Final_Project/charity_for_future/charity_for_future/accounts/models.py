from django.db import models


# Create your models here.

class Login(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )


class SignUp(models.Model):
    MAX_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
