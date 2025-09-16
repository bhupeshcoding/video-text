pythonlib

from moviepy.editor import VideoFileClip

clip = VideoFileClip("test.mp4")                # Loads the video file into memory
clip.audio.write_audiofile("test.wav")          # Extracts the audio track as WAV


