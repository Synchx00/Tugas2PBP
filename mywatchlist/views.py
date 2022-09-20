from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_film_list(request):
    data_watchlist = WatchListItem.objects.all()
    context = {
    'list_film': data_watchlist,
    'nama': 'Son Sulung Suryahatta Asnan',
    'id' : '2106751455'
    
}
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")