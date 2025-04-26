from django.shortcuts import render, redirect
import random
import string
from .models import LiveStream

# Create your views here.
def live_stream(request):
    return render(request,"video.html")

def start_streaming(request):
    # if request.method == "POST":
    N = 8  # Length of random room code
    room = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    LiveStream.objects.create(room=room)
    return redirect(f"/live-stream/?role=broadcaster&room={room}")
    # return render(request, "start_stream.html")


def streaming_list(request):
    all_streaming = LiveStream.objects.filter(is_streaming = True)
    return render(request, "streaming_list.html",{
        "streams" :all_streaming
    })
