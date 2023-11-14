from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='albums-home'),
    path('albumslist/', views.AlbumsListView.as_view(), name='album-list'),
    path('albumdetails/<int:pk>', views.AlbumsDetailView.as_view(), name='album-detail'),
]
