import os

import speech_recognition as sr

from pydub import AudioSegment


def convert_voice_to_text(ogg_file):

    wav_file = ogg_file.replace(
        ".ogg",
        ".wav"
    )

    audio = AudioSegment.from_ogg(
        ogg_file
    )

    audio.export(
        wav_file,
        format="wav"
    )

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:

        audio_data = recognizer.record(
            source
        )

        text = recognizer.recognize_google(
            audio_data
        )

    os.remove(ogg_file)

    os.remove(wav_file)

    return text