from pathlib import Path
import sys
import audio_extractor, transcribe

def main():
    video = Path(sys.argv[1])
    audio = audio_extractor.extract_audio(video, None)
    transcript = transcribe.transcribe(audio)
    print(transcript)

if __name__ == "__main__":
    main()
