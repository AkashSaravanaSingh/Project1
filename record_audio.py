
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=30, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print("Recording finished.")

record_audio(duration=30)