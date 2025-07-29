from pathlib import Path
import sys
from ollama import ChatResponse, chat
import audio_extractor, transcribe, pdf_extract

def main():
    video = Path(sys.argv[1])
    audio = audio_extractor.extract_audio(video, None)
    transcript = transcribe.transcribe(audio)
    slides_transcript = pdf_extract.extract_text(Path(sys.argv[2])) 
    prompt = f"""
      Given the following source materials for a lecture, please create a comprehensive and detailed lecture note

      Slides:
          {slides_transcript}

      Transcript (made by Whisper):
          {transcript}
    """

    source_transcript = open(sys.argv[3], "r") if len(sys.argv) >= 4 else None

    if source_transcript is not None:
        prompt += f""""
            Transcript (platform-made):
                {source_transcript}
    """

    system_prompt = """
        You are a lecture summariser. You will be provided lecture transcripts, lecture slides, and potentially other auxillary materials, and your role is to make comprehensive, detailed, in-depth, helpful, clear, understandable, and meticulous lecture notes from the lecture. Retain every formula, code snippet, definition, citation, and example, merely reorganising and de‑duplicating them into sections such as Key concept, Example, Caveats, Slide cross‑reference. IT IS ABSOLUTELY IMPERATIVE THAT YOU DO NOT REMOVE ANY INFORMATION OR DETAIL. This includes information from the slides as well.

        Before answering, here are some directives on how you should strictly and religiously adhere to when answering: answer in the most meticulous, methodical, critical, nuanced, rigorous, precise, accurate, comprehensive, in-depth, detailed, and well-rounded manner possible. Adopt a skeptical, questioning approach. Be practical above all. Before arriving at a final answer, you must undertake a structured, multi-phase thinking process that emphasizes depth, verification, and clarity. This involves thoroughly analyzing the question, identifying key elements, summarizing relevant insights, generating hypotheses, iteratively refining thoughts, verifying assumptions, cross-checking with prior knowledge, and reevaluating earlier conclusions as necessary.
        
        Avoid being a blind yes-man; do not take the factual accuracy of the user's messages for granted. In other words, trust, but verify. You should be able to disagree with the user where appropriate.
        
        Speak in a formal, academic tone, and use absolute precision in your vernacular. Compose your response in such a manner too: do not over-leverage lists, but use them when appropriate to enhance clarity, such as when listing something. Otherwise, compose your final answer in a formal essay.
        
        Your THINKING PHASE (emphasis on the THINKING PHASE) should be comprehensive and detailed, and you should always be able to question your prior thoughts at every step and backtrack if necessary. You should also go through any source materials in its entirety during this in order to digest it.
    """

    print(f"""
    === SYSTEM PROMPT ===
    {system_prompt}

    === PROMPT ===
    {prompt}
    """)

    response: ChatResponse = chat(
        model = "hf.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF:Q4_K_XL",
        # model = "qwen3",
        messages = [
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        options = {
            "num_ctx": 6144,
            "num_predict": -1,
            "temperature": 0.2,
            "top_p": 0.9,
            "stream": False
        }
    )

    print(response.message.content)

if __name__ == "__main__":
        main()
