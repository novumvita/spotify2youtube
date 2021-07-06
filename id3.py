import requests
import eyed3

def set_metadata(file_name, song, artist, album_art_url):

    print("Setting metadata.")
    audiofile = eyed3.load(file_name)
    tag = audiofile.tag

    tag.track = song

    tag.artist = artist

    img = requests.get(album_art_url[0]['url'], stream=True)
    img = img.raw

    albumart = img.read()
    tag.images.set(3, albumart, 'image/jpeg')

    tag.save(version=(2, 3, 0))
    print("Metadata set.")
    return