from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='albums-home'),
    # path('/albums/new', name='new-album'),
    path('album/<int:pk>', views.AlbumsDetailView.as_view(), name='album_detail'),
    # path('albumslist/', views.AlbumsListView.as_view(), name='album-list'),
    path('album/new_album', views.new_album, name='new_album')
]
