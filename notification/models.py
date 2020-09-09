from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    receiver = models.ForeignKey(
    TwitterUser, on_delete=models.CASCADE, related_name="receiver")
    msg_content = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
