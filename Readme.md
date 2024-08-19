# Minutes of the Meeting Generator

This project is a **Minutes of the Meeting Generator** that leverages speech-to-text technology, natural language processing, and machine learning to automatically generate meeting minutes from **audio recordings** or **live microphone input** . It includes features for summarizing the transcriptions, identifying speakers, and analyzing sentiment.

## Table of Contents

- [Project Summary](#project-summary)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Project Summary

The Minutes of the Meeting Generator automates the creation of meeting minutes by processing audio recordings. It transcribes the speech, identifies speakers, summarizes the content, and performs sentiment analysis. This project is designed to help professionals efficiently document and review meetings.

## Features

- **Speech-to-Text**: Converts spoken words from audio files into text with **Google Cloud's** `speech-to-text` API
- **Speaker Diarization**: dentifies different speakers in the audio file using Hugging Face's `pyannote` pipeline.
- **Summarization**: Automatically summarizes the transcribed text using **OpenAI's** GPT models.
- **Sentiment Analysis**: Analyzes the sentiment of the transcribed meeting content.
- **Real-Time Transcription**: Supports transcription from a live microphone feed.
- **Supports Multiple Audio Formats**: Handles common audio formats like WAV and MP3.

## Requirements

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.9+**
- **pip** 
- **virtualenv** 

### Python Packages

The following Python packages are required and will be installed during setup:

- `google-cloud-speech`
- `pyaudio`
- `openai`
- `transformers`
- `torch`
- `numpy`
- `absl-py`
- `matplotlib`
- `requests`

## Setup Instructions

### Step 1: Clone the Repository

```bash

git clone https://github.com/your-username/minutes-of-the-meeting-generator.git

cd minutes-of-the-meeting-generator
```
### Step 2: Set Up a Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Step 3: Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
If requirements.txt does not exist, create one with the necessary dependencies:


### Step 4: Set Up API Keys
#### Google Cloud Speech-to-Text API Key
- **Go to the Google Cloud Console**
- **Create a new project and enable the Speech-to-Text API.**
- **Create a service account key and download the JSON file.**
- **Set the GOOGLE_APPLICATION_CREDENTIALS environment variable:**

```bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
```
#### OpenAI API Key
- Sign up for an API key at OpenAI.
- Set the OPENAI_API_KEY environment variable:

```bash
Copy code
export OPENAI_API_KEY="your-api-key-here"
```

### Step 5: Run the Application
Once everything is set up, you can run the main script:

```bash
python src/main.py
```
## Usage
Transcription from Audio File
The application can transcribe and process an audio file to generate meeting minutes:

```python
generate_meeting_minutes(audio_source='file', audio_file='path_to_audio_file.wav')
```
Transcription from Microphone
The application can also transcribe and process live audio from a microphone:

```python
generate_meeting_minutes(audio_source='microphone')
```


## License
This project is licensed under the MIT License. See the LICENSE file for details.