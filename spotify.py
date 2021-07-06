from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy

scope = 'user-library-read'
client_credentials_manager = SpotifyClientCredentials()
sp1 = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def songs_finder(playlist_id):
    song = []
    song_name = []
    artist_name = []
    album_art_urls = []
    if playlist_id == "Liked":
        results = sp2.current_user_saved_tracks()
        playlist_name = "Liked_Songs"
        i = 0
        while True:
            for j in range(len(results['items'])):
                list = results['items'][j]['track']
                song_name.append(str(list['name']))
                artist_name.append(str(list['artists'][0]['name']))
                song.append(str(song_name[i]+'-'+artist_name[i]))
                album_art_urls.append(list['album']['images'])
                i += 1
                # print(i)
            if results['next']:
                results = sp2.next(results)
            else:
                break
    else:
        results = sp1.playlist(playlist_id)
        results = results['tracks']
        playlist_name = results['name']
        for i in range(len(results['items'])):
            list = results['items'][i]['track']
            song_name.append(str(list['name']))
            artist_name.append(str(list['artists'][0]['name']))
            song.append(str(song_name[i]+'-'+artist_name[i]))
            album_art_urls.append(list['album']['images'])
    return song, song_name, artist_name, album_art_urls, playlist_name

if __name__=="__main__":
    song_and_artist, song, artist, album_art_url, playlist = songs_finder()