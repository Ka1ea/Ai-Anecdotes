
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