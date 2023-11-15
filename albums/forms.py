from django import forms

import datetime


class NewAlbumForm(forms.Form):
    new_album_title = forms.CharField(label='Album Name', max_length=150)
    artist = forms.CharField(max_length=200)
    created_date = forms.DateField 
