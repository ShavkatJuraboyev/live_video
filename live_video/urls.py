from django.urls import path
from live_video.views import home

urlpatterns = [
    path('', home, name="home"),
]