import tweepy
import random
import lyricsgenius

autho = {'consumer_key': 'a',
         'consumer_secret': 'b',
         'key': 'b',
         'secret': 'c'}

def get_tkey():
    with open("tkey.txt", "r") as f:
        lines = f.read()
        return lines

def get_gkey():
    with open("gkey.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

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
    linep1 = lines[rand_num+1].lower()
    if linep1.find(r"[0-9]*embedshare URLCopyEmbedCopy") == True:
        linep1.replace(r"[0-100]*embedshare URLCopyEmbedCopy"," ")
    tweet = lines[rand_num] + "\n" + linep1 + " "
    tweet.replace(''''"''',''' ''')
    tweet = tweet.replace("\\", "")
    return tweet

def tweetIt():
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    t = api.update_status(tweet)
    id = t.id
    in_reply_to_status_id = str(id)
    api.update_status(song,in_reply_to_status_id)

s = get_tkey()
lines = s.split(',')
c = 0
for i in autho:
    autho.update({i: str(lines[c])})
    c += 1
auth = tweepy.OAuthHandler(autho['consumer_key'], autho['consumer_secret'])
auth.set_access_token(autho['key'], autho['secret'])
songs = ["XO", "​drugs", "Wake Up", "​sex (catching feelings)", "​rock + roll", "Gravity", "​crash", "Fumes", "​start//end", "Circles", "​forever//over", "​gold", "​love; not wrong (brave)", "​take care", "​wings", "​and", "​isohel", "​icarus", "Nocturne", "​falling in reverse", "​float", "​wonder", "​909", "​projector", "​love, death, distraction", "​wrong", "​lost//found", "​untitled", "​catch me if you can",
         "Interlude", "​hertz", "​nowhere else", "​just saying", "2020", "​how to sleep", "​good morning", "​fomo", "​about time​", "Peaked", "​rushing", "​so far so good", "02:09", "​calm down", "$treams", "​re//start", "​in", "​tides", "​static", "​out", "Amnesia", "Hey Ya", "​hello", "​running, tripping, falling (no future)", "XO (Extended)", "​all i want", "​call me back", "Dreaming About You"]
tweetIt()
exit()
