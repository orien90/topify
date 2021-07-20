import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6ce04d774cb14eb5a05990989db5dab1",
                                                           client_secret="921f09aa289240fbab1764f4a55ba7aa"))

songData = []
idList = {'ta': '37i9dQZF1DX1i3hvzHpcQV', 'no': '37i9dQZEVXbJvfa0Yxg7E7', 'en': '37i9dQZEVXbNG2KDcFcKOF',
          'kr': '41v7j1rKJmf2n0wBCWt43j'}


# current = sp.currently_playing()


def getSongs(id):
    results = sp.playlist_items(playlist_id=id, fields=None, limit=5, offset=0, market=None,
                                additional_types=('track',))
    for item in enumerate(results['items']):
        songInfo = []
        songInfo.append(item[1]['track']['album']['external_urls']['spotify'])
        songInfo.append(item[1]['track']['album']['images'][1]['url'])
        songInfo.append(item[1]['track']['album']['name'])
        songData.append(songInfo)


getSongs(idList.get('en'))


def songs(request):
    return render(request, "website/index.html",
                  {"results": songData})
