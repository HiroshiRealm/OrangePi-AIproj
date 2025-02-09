# 记得我运行这个项目的package都在新创建的一个venv里面, 不要忘记激活它
# 一个新环境中, 安装以下package
# pip install SpeechRecognition googletrans==4.0.0-rc1 pyttsx3 pyaudio

import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import os
from gs import inference, Language
from uuid import uuid4

landict = {
    Language.ZH: "zh-CN",
    Language.EN: "en",
    Language.JA: "ja"
}

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None
    
def test_speech(test_path):
    audio = sr.AudioFile(test_path)
    recognizer = sr.Recognizer()
    text = recognizer.recognize_google(audio)
    print(f"Recognized text: {text}")
    return text


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text


def synthesize_speech(text, language='en'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Default to English
    engine.say(text)
    engine.runAndWait()

#def synthesize_speech(text, language='zh-CN'):
    # gtts也是一个生成音频的选择. 
   #tts = gTTS(text=text, lang=language, slow=False)
    #tts.save("output.mp3")
    ## os.system("start output.mp3")  # For Windows; use 'open' for macOS or 'xdg-open' for Linux
    #playsound("output.mp3")

def real_time_translation(target_language):
    while True:
        print("Please speak now...")
        # recognized_text = recognize_speech_from_microphone()
        test_file = "data/input/test.wav"
        recognized_text = test_speech(test_file)
        if recognized_text:
            translated_text = translate_text(recognized_text, target_language=landict[target_language])
            output_path = f"data/output/{uuid4()}.wav"
            inference(ref_audio_path=test_file, prompt_text=recognized_text, prompt_language=Language.EN, text=translated_text, text_language=target_language, output_path=output_path)
        else:
            print("No speech recognized. Please try again.")

if __name__ == "__main__":
    real_time_translation(target_language=Language.ZH)  # Change 'zh-CN' to your target language code
