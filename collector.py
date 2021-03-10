import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import time
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('songHistory')


sp = spotipy.Spotify(auth_manager=config.sp)

interval = 0.2
#x = 1000
starttime = time.time()

temp = sp.current_playback()

#create dictionary
lastSong = {
    "trackName" : '',
    "artistName" : '',
    "albumName" : '',
    "msPlayed" : 999999999,
    "endTime" : ''
}
#fill dictionary with currently playing 
if (temp != None) :
    t = time.localtime()
    lastSong['trackName'] = temp['item']['name']
    lastSong['artistName'] = temp['item']['artists'][0]['name']
    lastSong['albumName'] = temp['item']['album']['name']
    lastSong['msPlayed'] = temp['progress_ms']
    lastSong['endTime'] = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2]) + " " + str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])

#run indefinetely until ctrl c
while True:
    
    time.sleep(interval - ((time.time() - starttime) % interval))
    #x -= interval
    temp = sp.current_playback()
    if(temp == None):
        print(temp, "", time.time())
    #make sure user is actually playing something
    if (temp != None) :

        t = time.localtime()

        #once songs changes
        if(temp['progress_ms'] < lastSong['msPlayed']) :
            #pass if it detects pause
            if (-temp['progress_ms'] * 0.001 + lastSong['msPlayed'] * 0.001) < 1.5 :
                pass
            #a new song
            else : 
                if temp != None :
                    #add new item in database
                    print(lastSong)
                    table.put_item(Item={
                    'endTime' : lastSong['endTime'],
                    'trackName' : lastSong['trackName'],
                    'artistName' : lastSong['artistName'],
                    'albumName' : lastSong['albumName'],
                    'msPlayed' : lastSong['msPlayed']
                    })
        if temp != None :
            lastSong['trackName'] = temp['item']['name']
            lastSong['artistName'] = temp['item']['artists'][0]['name']
            lastSong['albumName'] = temp['item']['album']['name']
            lastSong['msPlayed'] = temp['progress_ms']
            lastSong['endTime'] = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2]) + " " + str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])
