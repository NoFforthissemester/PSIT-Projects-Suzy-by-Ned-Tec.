import speech_recognition as sr
from gtts import gTTS

def suzy_speak(mess):
	tts = gTTS (mess=text, lang="en")
	name_f = "answer.mp3"
	tts.save(name_f)
	playsound.playsound(name_f)
speak("hello world suzy")
