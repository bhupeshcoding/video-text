import os
import sys
import wave
import numpy as np
from moviepy.editor import VideoFileClip
import soundfile as sf
from video_text import transcribe_video

def test_transcription():
    # Test with a sample video file (replace with your test video path)
    test_video = "test_video.mp"
    
    # Path to your Vosk model
    model_path = os.path.join(os.path.dirname(__file__), "models/vosk-model-small-en-us-0.15")
    
    if not os.path.exists(model_path):
        print(f"Error: Vosk model not found at {model_path}")
        print("Please download the model from https://alphacephei.com/vosk/models and extract it to the models/ directory")
        return
    
    if not os.path.exists(test_video):
        print(f"Error: Test video not found at {test_video}")
        print("Please provide a test video file")
        return
    
    print("Testing video transcription...")
    try:
        # Transcribe the video
        text, results = transcribe_video(test_video, model_path)
        
        print("\nTranscription successful!")
        print("\nTranscribed Text:")
        print("-" * 50)
        print(text)
        print("-" * 50)
        
        # Print some statistics
        word_count = sum(len(segment.get('result', [])) for segment in results if 'result' in segment)
        print(f"\nTranscription Statistics:")
        print(f"- Number of segments: {len(results)}")
        print(f"- Total words: {word_count}")
        print(f"- Total characters: {len(text)}")
        
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_transcription()
