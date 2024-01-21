import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
    body = {"text": message, "voice_settings": {"stability": 0, "similarity_boost": 0}}

    voice_shaun = "mTSvIrm2hmcnOvb21nW2"
    voice_leonor = "21m00Tcm4TlvDq8ikWAM"
    voice_antoni = "ErXwobaYiN019PkySvjV"

    # Construct request headers and url
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_leonor}"

    try:
        response = requests.post(endpoint, json=body, headers=headers)
        response.raise_for_status()  # Raises a HTTPError for certain status codes
        return response.content
    except requests.exceptions.HTTPError as http_err:
        # Handle specific HTTP errors (e.g., 4xx, 5xx responses)
        print(f"HTTP error occurred: {http_err}")
        raise http_err
    except Exception as e:
        # Handle other possible errors (e.g., network issues)
        print(f"Other error occurred: {e}")
        raise e
