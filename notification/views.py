from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notification.models import Notification


@login_required
def notifications(request):
    notification = Notification.objects.filter(receiver=request.user)
    for view in notification:
        view.delete()
    return render(request, "notifications.html", {'notification': notification})
