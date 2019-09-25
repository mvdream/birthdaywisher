from django.urls import path
from wishyou.views import *

app_name = 'wishyou'
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add/', PeopleView.as_view(), name="add"),
    path('mail/', SendMail.as_view(), name="sendmail"),
]
