

from pyannote.audio import Pipeline

def diarize_speakers(audio_file):
    print("Diarizing Speakers....")
    token = "#YOUR_HUGGING_FACE_TOKEN"  # Replace with your actual Hugging Face access token
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=token)

    diarization = pipeline(audio_file)

    speakers = {}
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        if speaker not in speakers:
            speakers[speaker] = ""
        speakers[speaker] += f"{turn.start:.1f}-{turn.end:.1f} {speaker}\n"
    print("Diarized speaker. Speakers found"+len(speakers))

    return speakers
