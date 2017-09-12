from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from models import *

def index(request):



  all_albums = Album.objects.all()
  html = ''

  for album in all_albums:
    url = '/music/' + str(album.id) + '/'
    html += '<a href="' + url + '">'  + album.album_title + '</a><br>'
    print html

  return HttpResponse(html)



def detail(request, album_id):

  return HttpResponse("<h2>Details for album_id: " + str(album_id) + "</h2>")
