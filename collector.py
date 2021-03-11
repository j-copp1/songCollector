import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import time, datetime
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('songHistory2')


sp = spotipy.Spotify(auth_manager=config.sp)

interval = 0.4
starttime = time.time()

#get initial song playing
temp = sp.current_playback()

#create dictionary
lastSong = {
    "trackName" : '',
    "artistName" : '',
    "albumName" : '',
    "msPlayed" : 999999999,
    "timePlayed" : 9999999
}
#fill dictionary with currently playing 
if (temp != None) :
    uTime = int(time.time())
    lastSong['trackName'] = temp['item']['name']
    lastSong['artistName'] = temp['item']['artists'][0]['name']
    lastSong['albumName'] = temp['item']['album']['name']
    lastSong['msPlayed'] = temp['progress_ms']
    lastSong['timePlayed'] = uTime


#run indefinetely until ctrl c
while True:

    time.sleep(interval - ((time.time() - starttime) % interval))

    temp = sp.current_playback()
    
    uTime = int(time.time())
    
    #make sure user is actually playing something
    #passes if temp is empty
    try :
        #once songs changes
        if(temp['progress_ms'] < lastSong['msPlayed']) :
            
            #pass if it detects pause
            if (-temp['progress_ms'] * 0.001 + lastSong['msPlayed'] * 0.001) < 1.5 :
                pass
            #a new song
            else : 
                #add new item in database
                print("added --->", lastSong)
                print("at --->", time.ctime(lastSong['timePlayed']))
                table.put_item(Item={
                'timePlayed' : lastSong['timePlayed'],
                'trackName' : lastSong['trackName'],
                'artistName' : lastSong['artistName'],
                'albumName' : lastSong['albumName'],
                'msPlayed' : lastSong['msPlayed']
                })
        lastSong['trackName'] = temp['item']['name']
        lastSong['artistName'] = temp['item']['artists'][0]['name']
        lastSong['albumName'] = temp['item']['album']['name']
        lastSong['msPlayed'] = temp['progress_ms']
        lastSong['timePlayed'] = uTime
    except(TypeError):
        pass
#uTime = time.time()
#print(uTime)
#print(time.ctime(uTime))