from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    post_time = models.DateTimeField(default=timezone.now)
    tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
