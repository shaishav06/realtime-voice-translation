import os
from flask import Flask, render_template, request, send_from_directory, Response, send_file
from werkzeug.utils import secure_filename
import speech_recognition as sr
from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile
from pydub import AudioSegment
from transcription import transcribe
from converter import convert_to_wav
from translation import translate

app = Flask(__name__)

# Disable caching for all routes
@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    response.cache_control.max_age = 0
    return response

# Create uploaded_files directory if it doesn't exist
if not os.path.exists(os.path.join('static','uploaded_files')):
    os.makedirs(os.path.join('static','uploaded_files'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload():
    print("entered ...")
    file = request.files["file-input"]
    if file.filename == "":
        return "No file selected."
    elif file:
        print("entered else")
        filename = secure_filename(file.filename)
        print("filename:",filename)
        file_path = os.path.join('static','uploaded_files', filename)

        file.save(file_path)

        # Convert to WAV format using converter.py
        # print("Reached the upload route","-"*10)
        # print("File path:", file_path)
        # print("Files in directory:", os.listdir(os.path.join('static','uploaded_files')))
        # print("Files in uploaded_files directory:", os.listdir(os.path.join('static','uploaded_files')))
        # print("\n\nzyx\n\n" , file_path)
        # # full_path = file_path.split(".")
        # # full_path[-1] = 'wav'
        # # output_file_path = '.'.join(full_path)
        output_file_path = file_path.replace( '.mp4' , ".wav" )
        print("output_file_path:",output_file_path)

        wav_file_path = convert_to_wav(file_path, output_file_path)
        print("wav_file_path:", wav_file_path)

        global transcription

        transcription = transcribe(wav_file_path) # returns string
        # transcription = transcribe(wav_file_path)
        # print(tr)
        target_language = request.form.get("language")

        global translation

        translation = translate(transcription,target_language)# returns list 0 th element is the translation
        print("transcription file type:",type(transcription))
        print("translation file type:", type(translation))
        return render_template("index.html", Transcription = transcription, Translation = translation[0])
        # return "done"

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ["mp3", "mp4"]


@app.route("/tp")
def tp():
    # wav_file_path = convert_to_wav(r"static\uploaded_files\sample1.mp4")
    # convert_to_wav( r"E:\BOOKS\Sem-8\Project\Sample Videos\how-ethics-can-help-you-make-better-decisions-ted-shorts-ted-426.mp4" , r"E:\BOOKS\Sem-8\Project\Sample Videos\how-ethics-can-help-you-make-better-decisions-ted-shorts-ted-426.wav" )

    return "done"

# Download Data
@app.route('/download/transcription/txt', methods=["GET", "POST"])
# @cross_origin()
def download_transcription():
    global transcription
    # with open("static/my_transcription.txt" , "w")  as f:
    #     f.write(transcription)
    response = Response(transcription, mimetype='text/plain')
    print(response)
    response.headers.set('Content-Disposition', 'attachment', filename='transcription.txt')
    return response
    # return send_file("static/my_transcription.txt")

@app.route('/download/translation/txt',methods = ["GET", "POST"])
def download_translation():
    global translation
    # with open("static/my_transcription.txt" , "w")  as f:
    #     f.write(transcription)    
    response = Response(translation[0], mimetype='text/plain')
    print(response)
    response.headers.set('Content-Disposition', 'attachment', filename='translation.txt')
    return response
    # return send_file("static/my_transcription.txt")


if __name__ == "__main__":
    app.run(debug=True)
