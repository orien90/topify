import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
import re

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6ce04d774cb14eb5a05990989db5dab1",
                                                           client_secret="921f09aa289240fbab1764f4a55ba7aa"))

#idList = {'ta': '37i9dQZF1DX1i3hvzHpcQV', 'no': '37i9dQZEVXbJvfa0Yxg7E7', 'en': '37i9dQZEVXbNG2KDcFcKOF',
          #'kr': '41v7j1rKJmf2n0wBCWt43j'}

song_data = []


# get four different playlist from Spotify
def get_all_songs(request):
    get_songs("37i9dQZF1DX1i3hvzHpcQV", "ta")
    get_songs("37i9dQZEVXbJvfa0Yxg7E7", "no")
    get_songs("37i9dQZEVXbNG2KDcFcKOF", "en")
    get_songs("41v7j1rKJmf2n0wBCWt43j", "kr")
    return render(request, "website/index.html",
                  {"results": get_songs})


def get_songs(id, lang):
    results = sp.playlist_items(playlist_id=id, fields=None, limit=5, offset=0, market=None,
                                additional_types=('track',))
    # appends each albums title, image and url to song_info
    for item in enumerate(results['items']):
        title = re.split(r'\([^)]*\)', item[1]['track']['album']['name'])
        title = title[0]
        song_info = []
        song_info.append(item[1]['track']['album']['external_urls']['spotify'])
        song_info.append(item[1]['track']['album']['images'][1]['url'])
        song_info.append(title)
        song_info.append(lang)
        if not song_info in song_data:
            song_data.append(song_info)
