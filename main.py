import spotify
import youtube
import ytdler
import sys
import os
import id3

if __name__=='__main__':
    playlist_id = sys.argv[1]
    if playlist_id == "Liked":
        song_and_artist, song, artist, album_art_url, playlist = spotify.songs_finder("Liked")
    else:
        song_and_artist, song, artist, album_art_url, playlist = spotify.songs_finder(playlist_id)
    playlist = '_'.join(playlist.split(' '))
    os.system(f'mkdir {playlist}')
    for i in range(len(song_and_artist)):
        video_ids = youtube.searcher(song_and_artist[i])
        print("Downloading...")
        try:
            try:
                video_url = 'https://www.youtube.com/watch?v='+video_ids[0]
                ytdler.downloader(video_url)
            except:
                video_url = 'https://www.youtube.com/watch?v='+video_ids[1]
                ytdler.downloader(video_url)
        except:
            print(f"Skipped {song[i]}({i+1} of {len(song_and_artist)}) due to an error.")
            continue
        print(f"Converted {song[i]}({i+1} of {len(song_and_artist)}).")
        os.system(f'mv *.mp3 "{playlist}/{song[i]}.mp3"')
        id3.set_metadata(f"{playlist}/{song[i]}.mp3", song[i], artist[i], album_art_url[i])