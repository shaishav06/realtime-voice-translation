import os
from converter import convert_to_wav
file_path = r"static\uploaded_files\my_result.mp3"

# Check file permissions
wav_file_path = convert_to_wav(file_path)

print(os.stat(file_path).st_mode)