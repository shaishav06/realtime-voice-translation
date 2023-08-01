import wave
import struct
import pyaudio
import os
import moviepy.editor as mp

def convert_to_wav(input_file, output_file):
    # Load the audio file using moviepy editor
    audio = mp.AudioFileClip(input_file)
    print("input_file:",input_file)
    print("output_file:", output_file)
    
    # Extract the audio from the file and save it to a temporary file
    temp_file = f"{input_file}.temp.wav"
    audio.write_audiofile(temp_file)
    
    # Open the temporary file in read mode
    with wave.open(temp_file, 'rb') as temp_wav:
        # Create a wave object for the output file
        with wave.open(output_file, 'wb') as output_wav:
            # Copy the parameters from the temporary file to the output file
            output_wav.setparams(temp_wav.getparams())
            
            # Read frames from the temporary file and write to the output file
            for i in range(temp_wav.getnframes()):
                frame = temp_wav.readframes(1)
                output_wav.writeframes(frame)
    return output_file
                
    # Delete the temporary file
    #os.remove(temp_file)
