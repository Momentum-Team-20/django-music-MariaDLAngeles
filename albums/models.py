from django.db import models
import datetime

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=500)
    artist = models.ForeignKey('artist', on_delete=models.RESTRICT, null=True)
    created_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title


# do we need this or is it  covered in album class?
# class Title(models.Model):
#     pass
    # album_title = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.album_title


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_name


# do we even need this or is it in album class?
# class CreatedDate(models.Model):
#     pass
    # created_on = models.DateField(auto_now=True)

    # def __str__(self):
    #     return f'This album was created on {self.created_on}'