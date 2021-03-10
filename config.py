import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

#authorization and refresh

#get from spotify development website
APP_CLIENT_ID = ""
APP_CLIENT_SECRET = ""

username = ''
client_id = APP_CLIENT_ID
client_secret = APP_CLIENT_SECRET
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-playback-state'

sp = SpotifyOAuth(client_id=APP_CLIENT_ID,
client_secret=APP_CLIENT_SECRET,
redirect_uri=redirect_uri,
scope=scope
)
