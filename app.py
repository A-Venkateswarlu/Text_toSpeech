from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')  # index.html must be in root

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text')
    lang = data.get('lang', 'en')

    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port)
