import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

#token for scope = user-read-recently-played
token = ''#'BQCyrF1yBxINzeaqcaWydq4VLqFukYqsVDwoY44gNjeM1QpBmvVP3iLC9_BNPddlSYMdqZlo0AdrL-BW40k6vybt44n8UHHsbYaAbHX8oyIbstm8YO9kTactDx6lZd4qEVF5igslB3BLL6aLkk3fLeQ'

#authorization and refresh

APP_CLIENT_ID = "2bc1e1e947d04af1b2c3694eff587cce"
APP_CLIENT_SECRET = "0f374e4638264192a60610c4417e50aa"

username = '1212132208'
client_id = APP_CLIENT_ID
client_secret = APP_CLIENT_SECRET
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-playback-state'

sp = SpotifyOAuth(client_id=APP_CLIENT_ID,
client_secret=APP_CLIENT_SECRET,
redirect_uri=redirect_uri,
scope=scope
)
