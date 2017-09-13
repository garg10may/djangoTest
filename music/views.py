from django.shortcuts import render, get_object_or_404
from django.http import Http404
from models import *

def index(request):

  all_albums = Album.objects.all()
  return render(request, 'music/index.html',  { 'all_albums': all_albums})

# def detail(request, album_id):
#   try:
#     album = Album.objects.get(pk=album_id)
#   except Album.DoesNotExist:
#     raise Http404("Album does not exist")
#   return render(request, 'music/detail.html', {'album':album})

def detail(request, album_id):
  album = get_object_or_404(Album, pk=album_id)
  return render(request, 'music/detail.html', {'album':album})


def favorite(request, album_id):
  album = get_object_or_404(Album, pk=album_id)