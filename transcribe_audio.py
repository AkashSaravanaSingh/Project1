import whisper

model = whisper.load_model("base")

def transcribe_audio(file_path):
    print(f"Transcribing file: {file_path}")
    result = model.transcribe(file_path, fp16=False, verbose=True)
    print("Full Whisper Output:", result)
    return result["text"]

# Transcribe the recorded audio
transcribed_text = transcribe_audio("output.wav")
print("\nTranscription:\n", transcribed_text)