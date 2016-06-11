import pyHook
import pythoncom
import configparser
from pyHook.HookManager import HookConstants
import spotipy
import spotipy.util as util
import requests
import time
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
parser = configparser.ConfigParser()
parser.read('config.ini')
parser.read(resource_path('api.ini'))
os.environ["SPOTIPY_CLIENT_ID"] = parser["api"]["SPOTIPY_CLIENT_ID"]
os.environ["SPOTIPY_REDIRECT_URI"] = parser["api"]["SPOTIPY_REDIRECT_URI"]
os.environ["SPOTIPY_CLIENT_SECRET"] = parser["api"]["SPOTIPY_CLIENT_SECRET"]



def OnKeyboardEvent(event):
    global parser
    global hm

    ctrl_pressed = pyHook.GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) >> 7
    alt_pressed = pyHook.GetKeyState(HookConstants.VKeyToID('VK_MENU')) >> 7
    if event.Key == "R":


        if ctrl_pressed and alt_pressed:
            hm.UnhookKeyboard()
            req = requests.get("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+parser["lastfm"]["user"]+ "&api_key="+parser["api"]["lastfm"]+"&format=json")
            reqJSON = req.json()
            curTrack = reqJSON['recenttracks']['track'][0]
            artist = curTrack['artist']["#text"]
            track = curTrack['name']
            req = requests.get("http://api.spotify.com/v1/search?q=track:" + track + "%20artist:" + artist + "&type=track")
            reqJSON = req.json()
            trackURI = reqJSON['tracks']['items'][0]['uri'].split(":")[2]
            trackURIs = [trackURI]
            username = parser['spotify']['userid']
            playlist_id = parser['spotify']['playlistid']
            scope = 'playlist-modify-public'
            token = util.prompt_for_user_token(username, scope)

            if token:
                sp = spotipy.Spotify(auth=token)
                sp.trace = False
                results = sp.user_playlist_add_tracks(username, playlist_id, trackURIs)
                print (results)
            else:
                print ("Can't get token for", username)
            hm.HookKeyboard()

    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()

pythoncom.PumpMessages()
hm.UnhookKeyboard()