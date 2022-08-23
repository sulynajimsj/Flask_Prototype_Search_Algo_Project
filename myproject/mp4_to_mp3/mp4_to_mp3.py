import moviepy
import moviepy.editor

def mp4_to_mp3(mp4VideoPath):
    # Get this library installed in your system

    # Import your video file
    # Media file should be local
    video = moviepy.editor.VideoFileClip(mp4VideoPath)    # Put your file path in here

    # Convert video to audio
    audio = video.audio
    audio.write_audiofile('new_audio.mp3')