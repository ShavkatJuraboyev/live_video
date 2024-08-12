from django.shortcuts import render
from .models import LiveVideo
# Create your views here.

def home(request):
    videos = LiveVideo.objects.all()
    return render(request, 'home.html', {'videos':videos})
