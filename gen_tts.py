from TTS.api import TTS
from pydub import AudioSegment

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

texts = [
    ("wolverines_start", "Wolverines, wake up"),
    ("wolverines_end", "Wolverines, close your eyes"),
    ("masons_start", "Masons, wake up"),
    ("masons_end", "Masons, close your eyes"),
]

DEFAULT_WAV_OUTPUT = "./sounds/output.wav"

for file_name, text in texts:
    tts.tts_to_file(
        text=text,
        speaker=tts.speakers[0],
        language=tts.languages[0],
        file_path=DEFAULT_WAV_OUTPUT,
    )
    AudioSegment.from_wav(DEFAULT_WAV_OUTPUT).export(f"./sounds/{file_name}.mp3", format="mp3")

import os

os.remove(DEFAULT_WAV_OUTPUT)