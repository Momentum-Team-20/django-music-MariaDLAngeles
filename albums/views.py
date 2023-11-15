from django.shortcuts import render
from django.views import generic
from .models import Album, Artist
from .forms import NewAlbumForm
from django.http import HttpResponseRedirect


# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})
# {albums: albums} is context data, dictionary-like and needed to for our albums to show up on our template


class AlbumsListView(generic.ListView):
    model = Album


class AlbumsDetailView(generic.DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


def new_album(request):
    if request.method == 'POST':
        form = NewAlbumForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
            # line 29 needs to change to the correct redirect
    else:
        form = NewAlbumForm()
    return render(request, 'new_album.html', {'form': form})