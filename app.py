# Call the function to separate audio and video
from Config import video_input_path, audio_output_path
from VideoLibrary import separate_audio_video

separate_audio_video(video_input_path, audio_output_path)

print(f"Done! You can find the audio in: {audio_output_path}")