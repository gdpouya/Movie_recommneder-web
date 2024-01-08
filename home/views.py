from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Playlist
from django.contrib import messages
from .forms import MovieCreateForm, MovieUpdateForm, PlaylistForm


def home(request):
	all_movies = Movie.objects.all()
	return render(request, 'home.html', {'movies': all_movies})


def detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	playlists = Playlist.objects.all()

	if request.method == 'POST':
		playlist_id = request.POST.get('playlist_id')
		playlist = get_object_or_404(Playlist, pk=playlist_id)
		playlist.movies.add(movie)
		playlist.save()

	return render(request, 'detail.html', {'movie': movie, 'playlists': playlists})


def delete(request, movie_id):
	Movie.objects.get(id=movie_id).delete()
	messages.success(request, 'movie deleted successfully', 'warning')
	return redirect('home')


def create(request):
	if request.method == 'POST':
		form = MovieCreateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			Movie.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
			messages.success(request, 'Movie created successfully', 'success')
			return redirect('home')
	else:
		form = MovieCreateForm()
	return render(request, 'create.html', {'form': form})


def update(request, movie_id):
	movie = Movie.objects.get(id=movie_id)
	if request.method == 'POST':
		form = MovieUpdateForm(request.POST, instance=movie)
		if form.is_valid():
			form.save()
			messages.success(request, 'your movie updated successfully', 'success')
			return redirect('details', movie_id)
	else:
		form = MovieUpdateForm(instance=movie)
	return render(request, 'update.html', {'form': form})


def playlist_list(request):
	playlists = Playlist.objects.all()
	return render(request, 'playlist_list.html', {'playlists': playlists})


def playlist_detail(request, playlist_id):
	playlist = get_object_or_404(Playlist, pk=playlist_id)
	return render(request, 'playlist_detail.html', {'playlist': playlist})


def create_playlist(request):
	if request.method == 'POST':
		form = PlaylistForm(request.POST)
		if form.is_valid():
			playlist = form.save()
			# You might want to associate the playlist with the current user
			# For example, if using Django's built-in user authentication:
			# playlist.user = request.user
			playlist.save()
			return redirect('playlist_list')  # Redirect to playlist list page
	else:
		form = PlaylistForm()
	return render(request, 'create_playlist.html', {'form': form})
