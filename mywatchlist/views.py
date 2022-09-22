from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_film_list(request):
    data_watchlist = WatchListItem.objects.all()

    watched = WatchListItem.objects.filter(watched="Watched")
    not_watched = WatchListItem.objects.filter(watched="Not watched")

    watched_count = watched.count()
    not_watched_count = not_watched.count()
    
    watched_status = watched_count >= not_watched_count

    context = {
    'list_film': data_watchlist,
    'nama': 'Son Sulung Suryahatta Asnan',
    'id' : '2106751455',
    'status_check' : watched_status,
}
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_home(request):
    return render(request, "mywatchlisthome.html")