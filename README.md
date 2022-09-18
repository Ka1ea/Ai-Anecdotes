# AI Anecdotes
## By: Kalea Gin, Catherine Park, Aashna Dureja, Rygel Ginete
### What It Does
Our website takes in a song name and artist, and outputs a website page containing the chorus of the song and a picture relating to the chorus. These images are generated by an AI called "Craiyon", an AI that when given a phrase, will output a generated image relating to the phrase. This gives the impression of the "story" of the song being presented in the perspective of an AI, thus our name "AI Anecdotes".
### How it Works / Technologies
Using a website made through HTML, CSS, Python, and Flask, the user input is received from the search bar and taken into Genius, which is a website that contains lyrics to thousands of songs. Our program then scans the lyrics to find the chorus (as prompted by the subheadings in Genius), and returns the chorus that is printed on the final webpage. Next, the program selects a random line from the chorus and inputs it into "Craiyon" automatically. After "Craiyon" generates the image, our program then extracts the source URL that projects the image on the final website.
