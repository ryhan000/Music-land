from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:song_id>/favorite/', views.favorite, name='favorite'),
    path('<int:album_id>/delete_album/', views.delete_album, name='delete_album'),
    path('album/add/', views.create_album, name='create_album'),
    path('<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name='delete_song'),

]
