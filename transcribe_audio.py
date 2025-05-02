import whisper

def transcribe_audio(file_path):
    # Load Whisper model
    model = whisper.load_model("base")

    # Transcribe audio file
    result = model.transcribe(file_path)
    return result["text"]

# Transcribe the recorded audio (output.wav)
transcribed_text = transcribe_audio("output.wav")
print("Transcription:\n", transcribed_text)