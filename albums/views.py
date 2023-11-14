from django.shortcuts import render
from django.views import generic
from .models import Album, Artist

# Create your views here.


def list_albums(request):
    return render(request, 'albums/index.html')


class AlbumsListView(generic.ListView):
    model = Album


class AlbumsDetailView(generic.DetailView):
    model = Album