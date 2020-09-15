from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.views.generic.base import View
import re


@login_required
def index(request):
    post_list = Tweet.objects.all().order_by('-post_time')
    pings = Notification.objects.filter(receiver=request.user)
    return render(request, "index.html", {"post_list": post_list, "pings": pings})


@login_required
def tweet_form(request):
    pings = Notification.objects.filter(receiver=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                body=data['body'], tweeter=request.user)
            if '@' in data['body']:
                recipient = re.findall(r'@(\w+)', data.get('body'))
                for receipt in recipient:
                    message = Notification.objects.create(msg_content=tweet, receiver=TwitterUser.objects.get(username=receipt))
            return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, "generic_form.html", {"form": form, "pings": pings})


# def tweet_detail(request, post_id):
#     if request.user.is_authenticated:
#         post = get_object_or_404(Tweet, id=post_id)
#         pings = Notification.objects.filter(receiver=request.user)
#         return render(request, 'tweet_detail.html', {'post': post, "pings": pings})
#     else:
#         return HttpResponseRedirect('public')

class TweetDetail(View):
    def get(self, request, post_id):
        if request.user.is_authenticated:
            post = get_object_or_404(Tweet, id=post_id)
            pings = Notification.objects.filter(receiver=request.user)
            return render(request, 'tweet_detail.html', {'post': post, "pings": pings})
        else:
            return HttpResponseRedirect('public')


def public_tweet(request, post_id):
    post = get_object_or_404(Tweet, id=post_id)
    return render(request, 'tweet_detail.html', {'post': post})
