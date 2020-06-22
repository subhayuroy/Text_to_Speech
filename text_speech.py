import pyttsx3

def onStart():
    print('starting')
def onWord(name, location, length):
    print('word', name, location, length)
def onEnd(name, completed):
    print('finishing', name, completed)

engine = pyttsx3.init()

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

sen = 'Subhayu Roy'

engine.say(sen)
engine.runAndWait()


#from gtts import gTTS
#import os

#mytext = 'Subhayu Roy'
#language = 'en'
#myobj = gTTS(text=mytext, lang=language, slow=False)
#myobj.save("wel.mp3")

# os.system('mpg321 wel.mp3 &')
# os.abort()
