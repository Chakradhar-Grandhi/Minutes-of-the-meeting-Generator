from summarization import generate_summary
from sentiment_analysis import analyze_sentiment, analyze_sentiment_with_hugging_face
from save_as_docx import save_as_docx
from transcription import transcribe_from_file, transcribe_from_microphone
import os
def generate_meeting_minutes(audio_source='file', audio_file=None):
    if audio_source == 'file' and audio_file:
        transcript = transcribe_from_file(audio_file)
    elif audio_source == 'microphone':
        transcript = transcribe_from_microphone()
    else:
        raise ValueError("Invalid audio source or missing audio file.")

    
    summary = generate_summary(transcript)

    try:
        sentiment_results = analyze_sentiment(transcript)
    except Exception as e:
        print(f"OpenAI failed with error: {e}. Falling back to Hugging Face.")
        sentiment_results = analyze_sentiment_with_hugging_face(transcript)

    save_as_docx(transcript, summary, sentiment_results)




audio_file_path = '#YOUR_AUDIO_FILE'
print(f"Resolved Path: {os.path.abspath(audio_file_path)}")
if not os.path.exists(audio_file_path):
    raise ValueError(f"File {audio_file_path} does not exist")

#For getting MOTM from audio recordings
#generate_meeting_minutes(audio_source='file', audio_file=audio_file_path)

# For microphone input:
#generate_meeting_minutes(audio_source='microphone')
