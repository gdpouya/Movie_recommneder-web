from django import forms
from .models import Movie, Playlist


class MovieCreateForm(forms.Form):
	title = forms.CharField()
	body = forms.CharField()
	created = forms.DateTimeField()


class MovieUpdateForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = '__all__'


class PlaylistForm(forms.ModelForm):
	class Meta:
		model = Playlist
		fields = ['name']
