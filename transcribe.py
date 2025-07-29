from logging import log
from pathlib import Path
from syslog import LOG_INFO
import whisper
from caching import persistent_cache

model_size = "turbo"

@persistent_cache
def transcribe(audio_file: Path) -> str:
    """
    Given an audio file, transcribe the speech to text.
    """
    log(LOG_INFO, f"Transcribing audio file {audio_file}")
    model = whisper.load_model(model_size)
    result = model.transcribe(f"{audio_file}")
    return result["text"]
