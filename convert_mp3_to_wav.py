import os
import sys
from pydub import AudioSegment


input_folder = sys.argv[1]
output_folder = sys.argv[2]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for file_name in os.listdir(input_folder):

    if file_name.endswith(".mp3"):

        mp3_file = AudioSegment.from_file(os.path.join(input_folder, file_name), format="mp3")

        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".wav")

        mp3_file.export(output_file, format="wav")
