from django.urls import path
from . import views

urlpatterns = [
    path("live-stream/", views.live_stream, name="stream"),  # ← add trailing slash
    path("start-stream/", views.start_streaming, name="start_stream"),
    path("", views.streaming_list, name="live_streaming_lis"),
]
