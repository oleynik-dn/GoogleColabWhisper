

import gdown
import openai
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def transcribe_audio():
    google_drive_file_id = request.args.get('google_drive_file_id')
    if not google_drive_file_id:
        return "Missing 'google_drive_file_id' parameter in the URL."

    google_drive_url = f'https://drive.google.com/uc?id={google_drive_file_id}'
    audio_file_name = 'audioFileName.mp3'  # Change this to match your desired file format


    # Rest of your code for transcription
    API_KEY = 'YOUR API_KEY'
    openai.api_key = API_KEY


    # Getting text from audio

    model_id = 'whisper-1'

    media_file_path = audio_file_name
    media_file = open(media_file_path, 'rb')

    response_0 = openai.Audio.transcribe(
        api_key=API_KEY,
        model=model_id,
        file=media_file,
        response_format='text' # text, json, srt, vtt
    )


    # Processing text from audio

    response_1 = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        # model="gpt-4",
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "Подведи итоги по встрече, и сформулируй основные задачи, которые нужно сделать, на основании следующего текста: "},
            {"role": "user", "content": response_0}
        ],
        max_tokens=4000
    )



    print('============================================================================')
    print(response_0)
    print('============================================================================')
    print(response_1["choices"][0]["message"]["content"])
    print('============================================================================')
    return response_0, response_1["choices"][0]["message"]["content"]


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
