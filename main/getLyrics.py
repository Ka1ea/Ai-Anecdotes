#pip install lyricsgenius

# search_song takes a user input and searches it genius then returns the song in lines
# find_chorus takes a series of lines and searches for the chorus and returns the chorus lines

from lyricsgenius import Genius

genius = Genius("nBPoYQZo2F3Pn0e4mO7FrCiPkJLLJSXgMKhbmkgAbRFwdfNCDQ5j90Gyi-USRy4H")

def search_song(input):
    lyrics = ""
    song = genius.search_song(input)
    return song.lyrics

def find_chorus(lyrics):
    chorus_start = lyrics.find("[Chorus") #int for first instance of Chrous
    chorus_string = lyrics[chorus_start:]#substring that starts at first Chorus
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