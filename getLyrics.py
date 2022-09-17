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
            print ("Stopped at " + line)
            break
        elif line.startswith("[") and not (line.startswith("[Chorus")):
            print ("Stopped at " + line)
            break
        else:
            chorus += line + "\n"
    print ("Done POG")
    return chorus

print ("Song pls")
userInput = input()
song = genius.search_song(userInput)

print ("Results for: " + userInput + " by " + song.artist)


geniusLyrics = song.to_text()

print(findChorus(geniusLyrics))
