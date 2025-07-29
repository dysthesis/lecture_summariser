from logging import log
from pathlib import Path
import sys
from syslog import LOG_INFO
import whisper

model_size = "turbo"

def transcribe(audio_file: Path) -> str:
    """
    Given an audio file, transcribe the speech to text.
    """
    log(LOG_INFO, f"Transcribing audio file {audio_file}")
    model = whisper.load_model(model_size)
    result = model.transcribe(f"{audio_file}")
    return result["text"]
