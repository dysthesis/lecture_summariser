from logging import log
from pathlib import Path
import subprocess
from syslog import LOG_INFO
import tempfile

def extract_audio(source: Path, workdir: Path | None) -> Path:
    """
    Extracts the audio from the video file at `source`. If given a `workdir`, it will output the 
    result there. Otherwise, it will create a temporary directory instead.
    """

    log(LOG_INFO, f"Extracting audio from {source}")
    if not source.is_file():
        raise FileNotFoundError(f"Input file not found: {source!s}")

    if workdir is None:
        workdir = Path(tempfile.mkdtemp())


    workdir.mkdir(parents=True, exist_ok=True)
    output_file = workdir / f"{source.stem}.wav"

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(source),
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        str(output_file)
    ]

    _ = subprocess.run(cmd, check=True)

    return output_file
