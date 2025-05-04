import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def record_audio(filename="output.wav", duration=10, fs=44100):
    print("Recording... Speak now.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    
    # Normalize audio volume (optional)
    recording = np.int16(recording / np.max(np.abs(recording)) * 32767)
    
    write(filename, fs, recording)
    print(f"Recording finished and saved to {filename}")

record_audio(duration=10)