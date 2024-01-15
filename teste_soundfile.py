from pydub import AudioSegment
import wave

def convert_to_wav(input_path, output_path):
    # Load the audio file with pydub
    audio = AudioSegment.from_file(input_path)

    # Convert pydub audio segment to raw PCM data
    raw_data = audio.raw_data
    sample_width = audio.sample_width
    frame_rate = audio.frame_rate
    channels = audio.channels

    # Write raw PCM data to a WAV file using wave module
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.writeframesraw(raw_data)
