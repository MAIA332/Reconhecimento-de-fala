from transcricao import recognize_speech
from download import teste
from teste_soundfile import convert_to_wav
import random
import json
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    name: str


def generate(audio_url):

    prefix = random.choice(range(0,10000))


    i_path = teste(audio_url)

    # Specify the path to the output WAV file
    output_wav_path = f"audio/{prefix}.wav"

    # Perform the conversion
    convert_to_wav(i_path, output_wav_path)

    print(f"Conversion complete. WAV file saved at: {output_wav_path}")

    a = recognize_speech(output_wav_path)
    return a

app = FastAPI()

@app.post("/extract/")
async def create_item(item: Item):
    b = generate(item.name)
    return b