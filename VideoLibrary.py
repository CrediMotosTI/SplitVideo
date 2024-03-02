from moviepy.editor import VideoFileClip

def separate_audio_video(video_path, audio_path):
    # Load the video
    video_clip = VideoFileClip(video_path)

    # Extract the audio
    audio_clip = video_clip.audio

    # Write the audio to a new file
    audio_clip.write_audiofile(audio_path)

    # Close the clips to release resources
    video_clip.close()
    audio_clip.close()