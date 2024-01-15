import whisper

model = whisper.load_model("base")
result = model.transcribe("494.wav")
print(result["text"])