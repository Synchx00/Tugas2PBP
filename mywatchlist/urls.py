import imp
from django.urls import path
from mywatchlist.views import show_film_list
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_home

app_name = 'mywatchlist'

urlpatterns = [

    path('', show_home, name='show_home'),
    path('html/', show_film_list, name='show_film_list'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]