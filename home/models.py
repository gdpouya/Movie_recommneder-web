from django.db import models


class Movie(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created = models.DateTimeField()


class Playlist(models.Model):
	name = models.CharField(max_length=100)
	movies = models.ManyToManyField(Movie)


