import tweepy
import random
import lyricsgenius

autho = {'consumer_key' : 'a' , 
         'consumer_secret' : 'b',
         'key' : 'b',
         'secret' : 'c'}
def get_tkey(): #module to acquire the twitter consumer key,secret key, API key and API secret key from the text file
    with open("tkey.txt","r") as f:
        lines = f.read()
        return lines
def get_gkey(): #module to acquire the genius access token from the text file
    with open("gkey.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
s = get_tkey()
lines = s.split(',')
c=0
for i in autho:
    autho.update({i:str(lines[c])})
    c+=1
auth = tweepy.OAuthHandler(autho['consumer_key'], autho['consumer_secret'])
auth.set_access_token(autho['key'], autho['secret'])
#manually added the songs to the list after searching them up using the artist.songs command
songs = ["XO","​drugs","Wake Up","​sex (catching feelings)", "​rock + roll", "Gravity", "​crash", "Fumes", "​start//end", "Circles", "​forever//over", "​gold", "​love; not wrong (brave)", "​take care", "​wings", "​and", "​isohel", "​icarus", "Nocturne", "​falling in reverse","​float", "​wonder", "​909", "​projector","​love, death, distraction", "​wrong", "​lost//found", "​untitled", "​catch me if you can", "Interlude", "​hertz", "​nowhere else", "​just saying", "2020", "​how to sleep", "​good morning","​fomo", "????", "​about time​", "Peaked", "​rushing", "​so far so good", "02 09", "​calm down", "$treams", "​re//start", "​in", "​tides", "​static", "​out", "Amnesia", "Hey Ya", "​hello", "​running, tripping, falling (no future)", "XO (Extended)", "​all i want", "​call me back*","Dreaming About You*"]
def get_raw_lyrics():
   genius_client_access_token = str(get_gkey())
   genius = lyricsgenius.Genius(genius_client_access_token)
   rand_song_title = random.choice(songs)
   lyrics = genius.search_song(rand_song_title, "EDEN").lyrics.lower()
   song = rand_song_title.lower() + " - EDEN"
   return lyrics, song
def get_tweet_from(lyrics):
   lines = lyrics.split('\n')
   for i in range(len(lines)):
       if lines[i] == "" or "[" in lines[i]:
           lines[i] = "XXX"
   lines = [i for i in lines if i != "XXX"]
   rand_num = random.randrange(0, len(lines)-1)
   tweet = lines[rand_num] + "\n" + lines[rand_num+1]
   tweet = tweet.replace("\\", "")
   return tweet

api = tweepy.API(auth)
lyrics, song = get_raw_lyrics()
tweet = get_tweet_from(lyrics)
api.update_status(tweet+"\n\n"+song)
