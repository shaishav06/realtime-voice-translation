

Project Description:


This project is a web application that allows users to upload an audio file (in MP3 or MP4 format), transcribe the speech in the audio file using Google Speech-to-Text API, and translate the transcription to a target language using the Helsinki-NLP/opus-mt model. The application is built using Flask and deployed locally on the user's machine. The transcription and translation can be downloaded as text files. The project can be useful for individuals who need to quickly transcribe and translate audio files for personal or professional use.

## Dependencies

- Flask
- SpeechRecognition
- transformers
- pydub
- moviepy


## Usage

To run the app, navigate to the project directory in your terminal and run `python app.py`. The app will run on http://localhost:5000/.

1. On the homepage, click the "Choose file" button to upload a video or audio file in .mp3 or .mp4 format.

2. Select the target language from the dropdown menu.

3. Click the "Transcribe and Translate" button to transcribe the speech in the file and translate the transcription to the target language.

4. The transcription and translation will be displayed on the homepage.

5. Click the "Download Transcription" or "Download Translation" button to download the transcription or translation in a text file.

## Credits

- The Google Speech Recognition API is used for transcription.
- The Hugging Face Transformers library is used for translation.
