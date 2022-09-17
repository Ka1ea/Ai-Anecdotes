#pip install lyricsgenius

from lyricsgenius import Genius

genius = Genius("nBPoYQZo2F3Pn0e4mO7FrCiPkJLLJSXgMKhbmkgAbRFwdfNCDQ5j90Gyi-USRy4H")

def findChorus(geniusLyrics):
    chorusStart = geniusLyrics.find("[Chorus]") #int for first instance of Chrous
    chorusString = geniusLyrics[chorusStart:]#substring that starts at first Chorus
    chorus = ""
    lines = chorusString.splitlines()
    for line in lines:
        if len(line.strip()) == 0:
            break
        elif line.startswith("[") and not (line.startswith("[Chorus]")):
            break
        else:
            chorus += line + "\n"

    return chorus

print ("Song pls")
userInput = input()
song = genius.search_song(userInput)

print ("Results for: " + userInput + " by " + song.artist)


geniusLyrics = song.to_text()

print(findChorus(geniusLyrics))
