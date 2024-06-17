import whisper


def voice_to_audio(voice):
    pass


def audio_to_text(audio):
    # 모델을 변수에 할당한다.
    model = whisper.load_model("tiny")

    """
    매개인자 voice를 모델이 해석 할 수 있는 형태로 바꾼다.
    하지만 mp3형태로 바꾼후 처리 할지 아니면 바로 들어온것을 처리가 가능 할지 의문.
    이점은 찾아보자.
    """
    text = model.transcribe(audio=audio)
