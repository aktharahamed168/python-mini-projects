import pyttsx3

# To save as MP3
# def text_to_speech(text):
#     engine = pyttsx3.init()

#     engine.setProperty("rate", 150)
#     engine.setProperty("volume", 1.0)

#     engine.save_to_file(text, "output.mp3")
#     engine.runAndWait()

def text_to_speech(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()


print("===== Text to Speech =====")

text = input("Enter text: ")

if text.strip():
    text_to_speech(text)
    print("\nText converted to speech successfully!")
else:
    print("\nPlease enter some text.")
