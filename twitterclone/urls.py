"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import index, tweeter, follow, unfollow, tweeter_view
from authentication.views import signup_view, login_view, logout_view
from tweet.views import index, tweet_form, tweet_detail, public_tweet
from notification.views import notifications

urlpatterns = [
    path('', index, name='homepage'),
    path('tweet/<int:post_id>/public/', public_tweet, name="public_tweet"),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('profile/<str:username>/public/', tweeter_view, name="public"),
    path('profile/<str:username>/', tweeter, name="profile"),
    path('tweetform/', tweet_form),
    path('tweet/<int:post_id>/', tweet_detail, name="tweet"),
    path('follow/<int:tweeter_id>/', follow),
    path('unfollow/<int:tweeter_id>/', unfollow),
    path('notifications/', notifications),
    path('admin/', admin.site.urls),
]
