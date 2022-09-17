# main.py
# main function that runs all the other code
# Team project by Ahsna Dureja, Catherine Park, Kalea Gin, Rygel Ginete
# 9/17/22
# version 1

from getLyrics import find_Chorus
from crayon import open_crayon

song = input("What song would you like to make a graphic about?")
lyrics = get_lyrics(song) #complete
select_lyrics = lyric_selector(lyrics) #pick 3 random lyrics from chorus
html = open_crayon(select_lyrics) #complete no debugs
links = get_image_links(html) #complete no debug
page = editOutput(lyrics, links)
