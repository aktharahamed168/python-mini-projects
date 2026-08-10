import speech_recognition as sr


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("\nSpeak something...")
        audio = recognizer.listen(source)

    try:
        print("\nConverting speech to text...")

        text = recognizer.recognize_google(audio)

        print("\nRecognized Text:")
        print(text)

    except sr.UnknownValueError:
        print("\nCould not understand the audio.")

    except sr.RequestError:
        print("\nSpeech recognition service is unavailable.")


print("===== Speech to Text =====")

speech_to_text()
