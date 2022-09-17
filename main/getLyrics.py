<<<<<<< HEAD:main/getLyrics.py

#pip install lyricsgenius

from lyricsgenius import Genius

genius = Genius("nBPoYQZo2F3Pn0e4mO7FrCiPkJLLJSXgMKhbmkgAbRFwdfNCDQ5j90Gyi-USRy4H")

def findChorus(geniusLyrics):
    chorusStart = geniusLyrics.find("Chorus") #int for first instance of Chrous
    chorusString = geniusLyrics[chorusStart:] #substring that starts at first Chorus
    lines = chorusString.splitlines()

    for line in lines:
        if len(line.strip()) == 0:
            break
        elif line.startswith("["):
            break
        else:
            print(line)
    
    #chorusEnd = chorusString.find("\n") #int
    #chorusString = geniusLyrics[chorusStart:chorusEnd]
    # return chorusString

print ("Song pls")
userInput = input()
song = genius.search_song(userInput)

print ("Results for: " + userInput + " by " + song.artist)

geniusLyrics = song.to_text()

findChorus(geniusLyrics)
=======
#pip install lyricsgenius

from lyricsgenius import Genius

genius = Genius("nBPoYQZo2F3Pn0e4mO7FrCiPkJLLJSXgMKhbmkgAbRFwdfNCDQ5j90Gyi-USRy4H")

def findChorus(genius_lyrics):
    chorus_start = genius_lyrics.find("[Chorus") #int for first instance of Chrous
    chorus_string = genius_lyrics[chorus_start:]#substring that starts at first Chorus
    chorus = ""
    lines = chorus_string.splitlines()
    for line in lines:
        if len(line.strip()) == 0:
            break
        elif line.startswith("[") and not (line.startswith("[Chorus")):
            break
        else:
            chorus += line + "\n"
    if chorus == "d\n":
        chorus = "No chorus found"
    return chorus

print ("Song pls")
user_input = input()
song = genius.search_song(user_input)

print ("Results for: " + user_input + " by " + song.artist)

genius_lyrics = song.to_text()

print(findChorus(genius_lyrics))
>>>>>>> f04e66fff04ad2dbe819fdd350f0402e7757f61c:getLyrics.py
