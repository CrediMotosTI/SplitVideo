# Paths for input and output files
import os

root_folder = r'C:\Users\jalva\Mi unidad\Motos\Credi Motos\Temporal\Videos\\'
video_input_folder = 'Video'
audio_output_folder = 'Audio'
video_input_name = 'f98e6466-a521-4f01-874c-5c0a8c65c4b6.mp4'

video_input_path = os.path.join(root_folder, video_input_folder, video_input_name)
audio_output_path = os.path.join(root_folder, audio_output_folder, os.path.splitext(video_input_name)[0] + '.mp3')
