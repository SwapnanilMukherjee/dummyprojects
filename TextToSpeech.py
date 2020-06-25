from gtts import gTTS
from playsound import playsound

text1 = input("Enter desired text\n")

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = text1, lang = language, slow = False)

sp.save(audio)
playsound(audio)
