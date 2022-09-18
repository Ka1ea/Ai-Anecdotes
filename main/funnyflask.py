from flask import Flask, render_template, request, jsonify
import json
from getLyrics import find_chorus, search_song
from crayon import open_crayon
from getData import get_image_links
from randomPhrase import rand_int

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def song_form():
    return render_template('simple.html')

@app.route('/song', methods=['POST'])
def my_form_post():
    data = json.loads(request.data.decode())['songName']
    song_data = search_song(data)
    chorus_data = ""
    if(song_data == None):
        return jsonify({'songImage': 'NONE'})
    else:
        chorus_data = find_chorus(song_data)
        print(chorus_data)

    # Get your image and set the song name
    # songImage = (chorus_data)
    imgs = open_crayon(chorus_data)
    

    songImage = imgs[rand_int(imgs)]

    return jsonify({'songImage': songImage, 'songChorus': chorus_data})

app.run(debug=True)