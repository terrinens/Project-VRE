import whisper
import pyaudio
from conversion_module import voice_to_audio


def waiting_call():
    pass


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024


def call_vrc():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    data = bytes

    for i in range(int(RATE / CHUNK)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    p.terminate()

    voice_to_audio(data)


def search_db():
    pass


def execution(path):
    pass
