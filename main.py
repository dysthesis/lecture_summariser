from pathlib import Path
import sys
import audio_extractor, transcribe, pdf_extract
from google import genai
from google.genai import types
import sys
import magic

def main():
    client = genai.Client()
    isVideo = lambda file: magic.from_file(file, mime=True).startswith('video/')
    isPdf = lambda file: magic.from_file(file, mime=True) == 'application/pdf'

    videos = list(filter(isVideo, map(Path, sys.argv)))
    slides = list(filter(isPdf, map(Path, sys.argv)))

    audios = [audio_extractor.extract_audio(video, Path("./test/COMP2041/work")) for video in videos]
    transcript = "\n".join([transcribe.transcribe(audio) for audio in audios])
    slides_transcript = "\n".join([pdf_extract.extract_text(slide) for slide in slides])

    prompt = f"""
      Given the following source materials for a lecture, please create a comprehensive and detailed lecture note

      Lecture transcript:
          {transcript}

      Slides:
          {slides_transcript}
    """

    system_prompt = """
        You are a lecture summariser. You will be provided lecture transcripts, lecture slides, and potentially other auxillary materials, and your role is to make comprehensive, detailed, in-depth, helpful, clear, understandable, and meticulous lecture notes from the lecture. Retain every formula, code snippet, definition, citation, and example, merely reorganising and de‑duplicating them into sections such as Key concept, Example, Caveats, Slide cross‑reference. IT IS ABSOLUTELY IMPERATIVE THAT YOU DO NOT REMOVE ANY INFORMATION OR DETAIL FROM THE LECTURE TRANSCRIPT. However, you should only mention contents of the slides when it is also mentioned in or otherwise relevant to the contents of the lecture transcript.

        Before answering, here are some directives on how you should strictly and religiously adhere to when answering: answer in the most meticulous, methodical, critical, nuanced, rigorous, precise, accurate, comprehensive, in-depth, detailed, and well-rounded manner possible. Adopt a skeptical, questioning approach. Be practical above all. Before arriving at a final answer, you must undertake a structured, multi-phase thinking process that emphasizes depth, verification, and clarity. This involves thoroughly analyzing the question, identifying key elements, summarizing relevant insights, generating hypotheses, iteratively refining thoughts, verifying assumptions, cross-checking with prior knowledge, and reevaluating earlier conclusions as necessary.
        
        Avoid being a blind yes-man; do not take the factual accuracy of the user's messages for granted. In other words, trust, but verify. You should be able to disagree with the user where appropriate.
        
        Speak in a formal, academic tone, and use absolute precision in your vernacular. Compose your response in such a manner too: do not over-leverage lists, but use them when appropriate to enhance clarity, such as when listing something. Otherwise, compose your final answer in a formal essay.
        
        Your THINKING PHASE (emphasis on the THINKING PHASE) should be comprehensive and detailed, and you should always be able to question your prior thoughts at every step and backtrack if necessary. You should also go through any source materials in its entirety during this in order to digest it.
    """

    response = client.models.generate_content_stream(
        model="gemini-2.5-pro",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=32768),
            system_instruction=system_prompt
        ),
        contents=prompt
    )

    for chunk in response:
        print(chunk.text, end="")


if __name__ == "__main__":
        main()
