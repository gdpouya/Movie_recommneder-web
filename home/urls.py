from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('details/<int:movie_id>/', views.detail, name='details'),
	path('delete/<int:movie_id>/', views.delete, name='delete'),
	path('update/<int:movie_id>', views.update, name='update'),
	path('create/', views.create, name='create'),
	path('movie/<int:movie_id>/', views.detail, name='movie_detail'),
	path('playlist/', views.playlist_list, name='playlist_list'),
	path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
	path('create_playlist/', views.create_playlist, name='create_playlist'),
]