from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class TwitterUser(AbstractUser):
    joined_date = models.DateField(auto_now_add=True)
    follows = models.ManyToManyField("self", symmetrical=False)
