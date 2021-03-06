from flask import Flask
from pydub import AudioSegment
from file import uploadFile

# initializing APP
app = Flask("MP3", static_url_path='/static', static_folder='static')


@app.route('/')
def index():
    fileName1 = 'path to file'
    fileName2 = 'path to file'
    song1 = AudioSegment.from_mp3(fileName1)
    song2 = AudioSegment.from_mp3(fileName2)
    combined = song1 + song2
    combinedFile = combined.export(format='mp3')
    uploadFile(combinedFile)
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)
