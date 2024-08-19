import requests
import os

# Ensure your OpenAI API key is stored in an environment variable
api_key = "#YOUR_OPEN_API_KEY"

def generate_summary(transcript):
    print("Generating Summary...")

    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Set up the data payload
    data = {
        "model": "gpt-4o-mini",  
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Please summarize the following transcript:\n{transcript}"
            }
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        
        response_data = response.json()
        summary = response_data['choices'][0]['message']['content']
        print("Generated Summary.")
        return summary
    else:
        error_message = f"Error: {response.status_code}, {response.text}"
        print(error_message)
        raise Exception(error_message)


