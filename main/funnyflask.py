from flask import Flask, render_template, request, jsonify
import json
from getLyrics import find_chorus, search_song

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def song_form():
    return render_template('simple.html')

@app.route('/song', methods=['POST'])
def my_form_post():
    data = json.loads(request.data.decode())['songName']
    song_data = search_song(data)
    if(song_data == None):
        return jsonify({'songImage': 'NONE'})
    else:
        chorus_data = find_chorus(song_data)
        print(chorus_data)

    # Get your image and set the song name
    # songImage = funky_ai_stuff(chorus_data)
    songImage = 'https://www.district158.org/wp-content/uploads/2019/04/hhs-front-entrance-dawn.jpg'

    return jsonify({'songImage': songImage, 'songChorus': chorus_data})

app.run(debug=True)