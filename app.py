from flask import Flask, request, send_file, render_template
from gtts import gTTS
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text')
    lang = data.get('lang', 'en')

    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
