import os
import requests

# import urllib
from django.shortcuts import render
from django.http import HttpResponse

from google.transit import gtfs_realtime_pb2

# Create your views here.


def index(request):
    return HttpResponse("Hello, World!")


def nqrw_feed(request):
    key = os.environ["MTA_KEY"]
    url = f"http://datamine.mta.info/mta_esi.php?feed_id=16&key={key}"

    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(url)
    print(f"Response: {response}")
    feed.ParseFromString(response.content)
    for entity in feed.entity:
        if entity.HasField("trip_update"):
            print(f"trip update: {entity.trip_update}")
    return render(request, "data/feed.html", {"feed": feed})
