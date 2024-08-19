import queue
import time
import logging
from google.cloud import speech
from google.api_core.exceptions import GoogleAPICallError, Unknown

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe_from_file(audio_file, diarization_result=None):
    print("Transcribing the file...")
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    streaming_config = speech.StreamingRecognitionConfig(config=config)

    def generate_stream(audio_file):
        print("Generating audio stream")
        with open(audio_file, 'rb') as audio_stream:
            while True:
                data = audio_stream.read(4096)
                if not data:
                    break
                yield speech.StreamingRecognizeRequest(audio_content=data)
                 # Simulate real-time streaming to prevent timeouts

    try:
        responses = client.streaming_recognize(streaming_config, generate_stream(audio_file))
        transcript = ""
        for response in responses:
            for result in response.results:
                transcript += f"{result.alternatives[0].transcript} "
        return transcript
    except GoogleAPICallError as e:
        logger.error(f"API call error: {e}")
        return ""
    except Unknown as e:
        logger.error(f"Unknown error during streaming: {e}")
        return ""
    except Exception as e:
        logger.error(f"General error: {e}")
        return ""

def transcribe_from_microphone(diarization_result=None):
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    streaming_config = speech.StreamingRecognitionConfig(config=config)

    audio_queue = queue.Queue()

    def callback(in_data, frame_count, time_info, status):
        audio_queue.put(in_data)
        return in_data, pyaudio.paContinue

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024,
                    stream_callback=callback)

    stream.start_stream()

    def generate_stream():
        while True:
            yield speech.StreamingRecognizeRequest(audio_content=audio_queue.get())

    transcript = ""
    try:
        responses = client.streaming_recognize(streaming_config, generate_stream())
        for response in responses:
            for result in response.results:
                transcript += f"{result.alternatives[0].transcript} "
    except GoogleAPICallError as e:
        logger.error(f"API call error: {e}")
    except Unknown as e:
        logger.error(f"Unknown error during streaming: {e}")
    except Exception as e:
        logger.error(f"General error: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    return transcript
